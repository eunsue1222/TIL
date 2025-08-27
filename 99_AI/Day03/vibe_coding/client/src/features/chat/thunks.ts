import { createAsyncThunk } from '@reduxjs/toolkit';
import { postChatMessage } from '../../services/chatApi';
import { uploadImageApi } from '../../services/uploadApi';
import { addMessage, setLoading } from './chatSlice';

interface SendMessagePayload {
  prompt: string;
  file: File | null;
}

export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async ({ prompt, file }: SendMessagePayload, { dispatch }) => {
    dispatch(setLoading(true));

    let imageUrl: string | undefined = undefined;
    let uploadedImagePath: string | undefined = undefined;

    // 1. If there is a file, upload it first.
    if (file) {
      try {
        const uploadResponse = await uploadImageApi(file);
        // The backend returns a relative path, construct the full URL
        const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
        imageUrl = `${apiBaseUrl}${uploadResponse.filePath}`;
        uploadedImagePath = uploadResponse.filePath; // Keep relative path for message object
      } catch (error) {
        console.error('Error uploading image:', error);
        dispatch(addMessage({ 
          id: Date.now().toString(), 
          text: 'Image upload failed. Please try again.', 
          sender: 'ai', 
          isError: true 
        }));
        dispatch(setLoading(false));
        return;
      }
    }

    // 2. Add user's message to chat history immediately.
    dispatch(addMessage({ 
      id: Date.now().toString(), 
      text: prompt, 
      sender: 'user',
      image: uploadedImagePath, // Use the relative path for the bubble
    }));

    // 3. Send the prompt and optional image URL to the chat API.
    try {
      const response = await postChatMessage({ input: prompt, imageUrl });
      
      // 4. Add AI's response to chat history.
      dispatch(addMessage({ id: (Date.now() + 1).toString(), text: response.output_text, sender: 'ai' }));
    } catch (error) {
      console.error('Error sending message:', error);
      dispatch(addMessage({ 
        id: (Date.now() + 1).toString(), 
        text: 'Error communicating with the AI. Please check your API key and server status.', 
        sender: 'ai',
        isError: true 
      }));
    } finally {
      dispatch(setLoading(false));
    }
  }
);

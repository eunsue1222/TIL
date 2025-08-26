import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
  image?: string; // Optional image URL
}

interface ChatState {
  chatHistory: Message[];
  currentPrompt: string;
  uploadedImage: string | null;
  isLoading: boolean;
}

const initialState: ChatState = {
  chatHistory: [],
  currentPrompt: '',
  uploadedImage: null,
  isLoading: false,
};

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage: (state, action: PayloadAction<Message>) => {
      state.chatHistory.push(action.payload);
    },
    setPrompt: (state, action: PayloadAction<string>) => {
      state.currentPrompt = action.payload;
    },
    uploadImage: (state, action: PayloadAction<string>) => {
      state.uploadedImage = action.payload;
    },
    clearImage: (state) => {
      state.uploadedImage = null;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
  },
});

export const { addMessage, setPrompt, uploadImage, clearImage, setLoading } = chatSlice.actions;
export default chatSlice.reducer;

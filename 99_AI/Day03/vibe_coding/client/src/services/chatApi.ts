import apiClient from './apiClient';

interface ChatPayload {
  input: string;
  imageUrl?: string; // Make imageUrl optional
}

interface ChatResponse {
  output_text: string;
}

export const postChatMessage = async (payload: ChatPayload): Promise<ChatResponse> => {
  const response = await apiClient.post('/api/chat', payload);
  return response.data;
};

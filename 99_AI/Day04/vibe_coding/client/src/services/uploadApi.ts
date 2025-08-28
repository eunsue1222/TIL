import apiClient from './apiClient';

export const uploadImageApi = async (file: File): Promise<{ filePath: string }> => {
  const formData = new FormData();
  formData.append('image', file);

  const response = await apiClient.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

  return response.data;
};

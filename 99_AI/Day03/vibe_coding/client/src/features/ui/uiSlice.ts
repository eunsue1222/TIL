import { createSlice } from '@reduxjs/toolkit';

interface UiState {
  // Define UI state properties here, e.g.,
  // isMenuOpen: boolean;
}

const initialState: UiState = {
  // isMenuOpen: false,
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    // Define UI-related reducers here
  },
});

// export const { ... } = uiSlice.actions;
export default uiSlice.reducer;

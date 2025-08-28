import React from 'react';
import MessageList from '../../components/Chat/MessageList/MessageList';
import MessageInput from '../../components/Chat/MessageInput/MessageInput';

const ChatPage: React.FC = () => {
  return (
    <div className="d-flex flex-column vh-100">
      <MessageList />
      <MessageInput />
    </div>
  );
};

export default ChatPage;
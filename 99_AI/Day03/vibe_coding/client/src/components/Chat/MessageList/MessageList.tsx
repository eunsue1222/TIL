import React, { useEffect, useRef } from 'react';
import { useAppSelector } from '../../../app/hooks';
import MessageBubble from '../MessageBubble/MessageBubble';
import LoadingBubble from '../LoadingBubble/LoadingBubble';

const MessageList: React.FC = () => {
  const { chatHistory, isLoading } = useAppSelector((state) => state.chat);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory, isLoading]);

  return (
    <div className="flex-grow-1 p-4" style={{ overflowY: 'auto', paddingBottom: '100px' }}>
      {chatHistory.map((message) => (
        <MessageBubble key={message.id} message={message} />
      ))}
      {isLoading && <LoadingBubble />}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default MessageList;

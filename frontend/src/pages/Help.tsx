
import React from "react";

const Help: React.FC = () => {
  return (
    <div className="container mx-auto p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Help & Documentation</h1>
        
        <div className="space-y-8">
          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">Getting Started</h2>
            <p className="mb-4 text-gray-700">
              Welcome to Learning Assistant! This guide will help you navigate through the application and make the most of its features.
            </p>
            <ol className="list-decimal list-inside space-y-2 text-gray-700">
              <li>Start by uploading your PDF documents from the Dashboard.</li>
              <li>Once uploaded, you can ask questions related to the content of those PDFs.</li>
              <li>Your conversations are organized into folders for easy reference.</li>
              <li>Use the voice chat feature when you prefer speaking over typing.</li>
            </ol>
          </section>

          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">PDF Upload</h2>
            <p className="text-gray-700 mb-4">
              You can upload PDFs containing your study materials, lecture notes, or any content you want to query later.
            </p>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Click the "Upload a PDF" button on your dashboard.</li>
              <li>Select the PDF file from your device.</li>
              <li>The system will process the PDF and make its content available for queries.</li>
              <li>You can upload multiple PDFs and switch between them during conversations.</li>
            </ul>
          </section>

          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">Chat Interface</h2>
            <p className="text-gray-700 mb-4">
              The chat interface allows you to ask questions about your uploaded PDFs.
            </p>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Type your question in the input field at the bottom of the chat.</li>
              <li>The system will search through your PDF content for relevant answers.</li>
              <li>If an answer isn't found in your PDFs, the system will search the web for additional information.</li>
              <li>Use the "Talk" button to ask questions using voice input.</li>
            </ul>
          </section>

          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">Folder Management</h2>
            <p className="text-gray-700 mb-4">
              Keep your conversations organized by using the folder system.
            </p>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Create new folders by clicking the "+" icon in the sidebar.</li>
              <li>Name your folders based on subjects, projects, or any category that helps organize your work.</li>
              <li>Move chats between folders for better organization.</li>
              <li>Rename folders as needed to keep your workspace tidy.</li>
            </ul>
          </section>

          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">Profile Management</h2>
            <p className="text-gray-700 mb-4">
              Update your profile information and manage your account settings.
            </p>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Click on your profile icon in the sidebar to access your profile page.</li>
              <li>Update your name, email, or password as needed.</li>
              <li>Manage notification preferences and application settings.</li>
              <li>Log out from your account when necessary.</li>
            </ul>
          </section>

          <section className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-semibold text-purple-600 mb-4">Need More Help?</h2>
            <p className="text-gray-700">
              If you have additional questions or need further assistance, please contact our support team at support@learningassistant.com.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
};

export default Help;


import React from "react";
import { NavLink } from "react-router-dom";
import { Home, HelpCircle, PanelLeft } from "lucide-react";
import { Button } from "@/components/ui/button";
import { useSidebar } from "@/components/ui/sidebar";

const TopBar: React.FC = () => {
  const { state, toggleSidebar } = useSidebar();

  return (
    <div className="sticky top-0 z-10 w-full bg-white border-b border-gray-200 shadow-sm">
      <div className="flex items-center justify-between px-4 py-2">
        <div className="flex items-center space-x-4">
          {/* Only show the expand sidebar button when sidebar is collapsed */}
          {state === "collapsed" && (
            <Button 
              variant="ghost" 
              size="icon" 
              className="h-8 w-8" 
              onClick={toggleSidebar}
            >
              <PanelLeft className="h-5 w-5" />
              <span className="sr-only">Expand Sidebar</span>
            </Button>
          )}
          <div className="font-bold text-xl text-purple-500">Learning Assistant</div>
        </div>
        
        <div className="flex items-center space-x-2">
          <NavLink 
            to="/dashboard" 
            className={({ isActive }) => `
              flex items-center px-3 py-2 rounded-md text-sm font-medium
              ${isActive ? 'text-purple-500' : 'text-gray-600 hover:text-purple-500'}
            `}
          >
            <Home className="h-4 w-4 mr-1" />
            <span>Home</span>
          </NavLink>
          
          <NavLink 
            to="/help" 
            className={({ isActive }) => `
              flex items-center px-3 py-2 rounded-md text-sm font-medium
              ${isActive ? 'text-purple-500' : 'text-gray-600 hover:text-purple-500'}
            `}
          >
            <HelpCircle className="h-4 w-4 mr-1" />
            <span>Help</span>
          </NavLink>
        </div>
      </div>
    </div>
  );
};

export default TopBar;

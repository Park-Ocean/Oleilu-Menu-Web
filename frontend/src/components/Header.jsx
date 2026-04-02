import React from 'react';
import { Search, X, Instagram } from 'lucide-react';

export default function Header({ 
  isAdmin, 
  onLogoClick, 
  searchQuery, 
  onSearchChange, 
  onLogout 
}) {
  return (
    <div className="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-[#DBCBB4] shadow-sm">
      <div className="max-w-4xl mx-auto px-4 py-4">

        <div className="flex items-center justify-between mb-4">
          <div 
            onClick={onLogoClick}
            className="cursor-pointer select-none flex flex-col items-start"
          >
            <div className="flex flex-col items-center">
              <span className="font-sans font-light text-sm tracking-[0.3em] text-[#423838]">COFFEE</span>
              <span className="font-sans font-black text-4xl tracking-tight text-[#1a1a1a] leading-none">BEANS</span>
              <span className="font-sans font-normal text-sm tracking-[0.3em] text-[#423838] mt-1">CHILE</span>
            </div>
            <div className="flex gap-1 mt-2 mb-1 w-full justify-center">
              <div className="w-6 h-1 bg-[#F9D030]"></div>
              <div className="w-6 h-1 bg-[#4CAF50]"></div>
              <div className="w-6 h-1 bg-[#2196F3]"></div>
              <div className="w-6 h-1 bg-[#FF9800]"></div>
            </div>
            <span className="font-display text-[10px] font-bold uppercase tracking-[0.2em] text-[#8D7A6A] mt-1 self-center">
              {isAdmin ? "PANEL DE CONTROL" : "MENÚ"}
            </span>
          </div>


          {isAdmin ? (
            <button 
              onClick={onLogout} 
              className="bg-[#50768C] text-white px-4 py-2 rounded-xl text-xs font-bold shadow-sm active:scale-95 transition-transform hover:bg-[#3B596A]"
            >
              Salir
            </button>
          ) : (
            <a 
              href="https://www.instagram.com/Coffee Beanspasteleria/" 
              target="_blank" 
              rel="noreferrer"
              className="text-[#8D7A6A] hover:text-[#50768C] transition-colors p-2"
            >
              <Instagram size={24} strokeWidth={1.5} />
            </a>
          )}
        </div>


        <div className="relative">
          <Search 
            className="absolute left-4 top-1/2 -translate-y-1/2 text-[#8D7A6A]" 
            size={18} 
          />
          <input
            type="text"
            placeholder="Buscar productos..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            className="w-full pl-12 pr-10 py-3 bg-[#F5EBE1] border border-[#DBCBB4] rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-[#50768C]/20 transition-all"
          />
          {searchQuery && (
            <button
              onClick={() => onSearchChange('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-[#8D7A6A] hover:text-[#50768C] p-1"
            >
              <X size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

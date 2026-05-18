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
    <div className="sticky top-0 z-50 bg-[#0d2096]/95 backdrop-blur-sm border-b border-[#0d2096] shadow-sm">
      <div className="max-w-4xl mx-auto px-4 py-4">

        <div className="flex items-center justify-between mb-4">
          <div
            onClick={onLogoClick}
            className="cursor-pointer select-none flex flex-col items-start"
          >
            <div className="flex items-center gap-3">
              <div className="flex flex-col items-start">
                <span className="font-sans font-black text-4xl tracking-tight text-[#fcfcfc] leading-none">OLEILU</span>
              </div>
            </div>

            <span className="font-display text-[10px] font-bold uppercase tracking-[0.2em] text-[#fcfcfc]/80 mt-1 self-center">
              {isAdmin ? "PANEL DE CONTROL" : "MENÚ"}
            </span>
          </div>


          {isAdmin ? (
            <button
              onClick={onLogout}
              className="bg-[#fcfcfc] text-[#0d2096] px-4 py-2 rounded-xl text-xs font-bold shadow-sm active:scale-95 transition-transform hover:bg-white"
            >
              Salir
            </button>
          ) : (
            <a
              href="https://www.instagram.com/oleilu.cl/"
              target="_blank"
              rel="noreferrer"
              className="text-[#fcfcfc] hover:text-white transition-colors p-2"
            >
              <Instagram size={24} strokeWidth={1.5} />
            </a>
          )}
        </div>


        <div className="relative">
          <Search
            className="absolute left-4 top-1/2 -translate-y-1/2 text-[#0d2096]"
            size={18}
          />
          <input
            type="text"
            placeholder="Buscar productos..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            className="w-full pl-12 pr-10 py-3 bg-[#fcfcfc] border border-transparent rounded-2xl text-sm focus:outline-none focus:ring-2 focus:ring-white/50 transition-all text-[#0d2096] placeholder:text-[#0d2096]/60"
          />
          {searchQuery && (
            <button
              onClick={() => onSearchChange('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-[#0d2096] hover:text-[#0d2096]/70 p-1"
            >
              <X size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

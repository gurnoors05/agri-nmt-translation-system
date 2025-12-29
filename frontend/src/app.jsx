import React, { useState } from 'react';
import { Send, Copy, Check, AlertCircle, Loader2, Languages, Sprout, Wheat, ArrowRight } from 'lucide-react';

export default function AgriTranslatorApp() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const translateText = async (text) => {
    const response = await fetch('http://localhost:8000/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text }),
    });

    if (!response.ok) {
      throw new Error('Translation failed. Please check if the backend server is running.');
    }

    const data = await response.json();
    return data.hindi;
  };

  const handleTranslate = async () => {
    if (!inputText.trim()) {
      setError('Please enter some text to translate');
      return;
    }

    setLoading(true);
    setError('');
    setOutputText('');

    try {
      const result = await translateText(inputText);
      setOutputText(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = async () => {
    if (outputText) {
      await navigator.clipboard.writeText(outputText);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const handleClear = () => {
    setInputText('');
    setOutputText('');
    setError('');
  };

  const exampleTexts = [
    'Apply urea fertilizer in split doses for better nitrogen management.',
    'Spray fungicide on tomato plants to prevent early blight disease.',
    'Strong winds can uproot banana plantations during cyclonic weather.',
    'Upload your Aadhaar card on the agriculture portal for subsidy verification.',
  ];

  const loadExample = (text) => {
    setInputText(text);
    setOutputText('');
    setError('');
  };

  return (
    <div className="min-h-screen relative overflow-hidden bg-gradient-to-br from-emerald-900 via-green-800 to-teal-900">
      {/* Animated Background Pattern */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-0 left-0 w-96 h-96 bg-green-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse" />
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-emerald-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse" style={{ animationDelay: '1000ms' }} />
        <div className="absolute top-1/2 left-1/2 w-96 h-96 bg-teal-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse" style={{ animationDelay: '500ms' }} />
      </div>

      {/* Decorative Wheat Icons */}
      <div className="absolute top-10 left-10 opacity-5">
        <Wheat className="w-40 h-40 text-white" />
      </div>
      <div className="absolute bottom-10 right-10 opacity-5">
        <Sprout className="w-40 h-40 text-white" />
      </div>

      <div className="relative z-10 min-h-screen p-4 md:p-8">
        <div className="max-w-7xl mx-auto">
          {/* Header */}
          <div className="text-center mb-12 mt-8">
            <div className="inline-flex items-center gap-4 mb-6 bg-white/10 backdrop-blur-xl px-8 py-4 rounded-full border border-white/20">
              <Languages className="w-12 h-12 text-emerald-300" />
              <div className="text-left">
                <h1 className="text-4xl md:text-5xl font-black text-white tracking-tight">
                  Krishi Anuvadak
                </h1>
                <p className="text-emerald-200 text-sm font-medium">कृषि सलाहकार अनुवादक</p>
              </div>
            </div>
            <p className="text-white/90 text-lg font-medium">
              Smart AI-Powered English to Hindi Agricultural Translation
            </p>
          </div>

          {/* Main Translation Interface */}
          <div className="mb-8">
            <div className="grid lg:grid-cols-2 gap-6">
              {/* English Input */}
              <div className="group">
                <div className="bg-gradient-to-br from-white/95 to-blue-50/95 backdrop-blur-xl rounded-3xl shadow-2xl border border-white/50 p-6 md:p-8 transition-all duration-300 hover:shadow-emerald-500/20 hover:scale-[1.01]">
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-blue-500 rounded-2xl flex items-center justify-center shadow-lg">
                        <span className="text-white font-bold text-sm">EN</span>
                      </div>
                      <div>
                        <h3 className="text-base md:text-lg font-bold text-gray-800">English</h3>
                        <p className="text-xs text-gray-500">Source Language</p>
                      </div>
                    </div>
                    <span className="text-xs font-semibold text-gray-500 bg-gray-100 px-3 py-1.5 rounded-full">
                      {inputText.length} characters
                    </span>
                  </div>
                  
                  <div className="relative">
                    <textarea
                      value={inputText}
                      onChange={(e) => setInputText(e.target.value)}
                      placeholder="Type or paste your agricultural advisory text here...

Example:
• Fertilizer recommendations
• Pest control measures
• Weather advisories
• Government scheme information"
                      className="w-full h-64 md:h-80 p-4 md:p-6 bg-white/80 backdrop-blur-sm border-2 border-gray-200/50 rounded-2xl focus:border-blue-400 focus:ring-4 focus:ring-blue-400/20 focus:outline-none resize-none text-gray-800 text-sm md:text-base leading-relaxed transition-all placeholder:text-gray-400 shadow-inner"
                      disabled={loading}
                    />
                  </div>
                </div>
              </div>

              {/* Hindi Output */}
              <div className="group">
                <div className="bg-gradient-to-br from-white/95 to-emerald-50/95 backdrop-blur-xl rounded-3xl shadow-2xl border border-white/50 p-6 md:p-8 transition-all duration-300 hover:shadow-emerald-500/20 hover:scale-[1.01]">
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl flex items-center justify-center shadow-lg">
                        <span className="text-white font-bold text-sm">HI</span>
                      </div>
                      <div>
                        <h3 className="text-base md:text-lg font-bold text-gray-800">हिंदी (Hindi)</h3>
                        <p className="text-xs text-gray-500">Target Language</p>
                      </div>
                    </div>
                    {outputText && (
                      <button
                        onClick={handleCopy}
                        className="flex items-center gap-2 text-xs font-bold text-emerald-700 hover:text-emerald-600 bg-emerald-100 hover:bg-emerald-200 px-3 md:px-4 py-1.5 md:py-2 rounded-full transition-all shadow-md hover:shadow-lg"
                      >
                        {copied ? (
                          <>
                            <Check className="w-3.5 md:w-4 h-3.5 md:h-4" />
                            <span className="hidden sm:inline">Copied!</span>
                          </>
                        ) : (
                          <>
                            <Copy className="w-3.5 md:w-4 h-3.5 md:h-4" />
                            <span className="hidden sm:inline">Copy</span>
                          </>
                        )}
                      </button>
                    )}
                  </div>
                  
                  <div className="relative">
                    <textarea
                      value={outputText}
                      readOnly
                      placeholder="आपका अनुवाद यहां दिखाई देगा...
(Your translation will appear here)

हमारा AI मॉडल सटीक अनुवाद प्रदान करता है।"
                      className="w-full h-64 md:h-80 p-4 md:p-6 bg-gradient-to-br from-green-50/80 to-emerald-50/80 backdrop-blur-sm border-2 border-emerald-200/50 rounded-2xl resize-none text-gray-800 text-sm md:text-base leading-relaxed shadow-inner placeholder:text-gray-400"
                    />
                    
                    {/* Decorative Element */}
                    {outputText && (
                      <div className="absolute bottom-4 right-4 bg-emerald-500 text-white px-3 py-1 rounded-full text-xs font-bold shadow-lg">
                        ✓ Translated
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Center Arrow and Translate Button */}
            <div className="flex justify-center -mt-4 mb-4 relative z-20">
              <div className="bg-white/95 backdrop-blur-xl rounded-full p-2 shadow-2xl border-4 border-emerald-500/30">
                <button
                  onClick={handleTranslate}
                  disabled={loading || !inputText.trim()}
                  className="bg-gradient-to-r from-emerald-500 via-green-500 to-teal-500 text-white w-16 h-16 md:w-20 md:h-20 rounded-full font-bold hover:from-emerald-600 hover:via-green-600 hover:to-teal-600 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed transition-all shadow-xl hover:shadow-2xl hover:scale-110 active:scale-95 flex items-center justify-center"
                >
                  {loading ? (
                    <Loader2 className="w-6 h-6 md:w-8 md:h-8 animate-spin" />
                  ) : (
                    <ArrowRight className="w-6 h-6 md:w-8 md:h-8" />
                  )}
                </button>
              </div>
            </div>

            {/* Action Buttons Row */}
            <div className="flex justify-center gap-4">
              <button
                onClick={handleClear}
                disabled={loading}
                className="px-6 md:px-8 py-2.5 md:py-3 bg-white/20 backdrop-blur-xl text-white font-bold text-sm md:text-base rounded-full hover:bg-white/30 disabled:opacity-50 disabled:cursor-not-allowed transition-all border border-white/30 shadow-lg"
              >
                Clear All
              </button>
            </div>

            {/* Error Message */}
            {error && (
              <div className="mt-6 mx-auto max-w-2xl p-4 md:p-6 bg-red-500/90 backdrop-blur-xl border-2 border-red-400/50 rounded-3xl flex items-start gap-3 md:gap-4 shadow-2xl">
                <div className="bg-white/20 rounded-full p-2 flex-shrink-0">
                  <AlertCircle className="w-5 h-5 md:w-6 md:h-6 text-white" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm md:text-base font-bold text-white">Translation Error</p>
                  <p className="text-xs md:text-sm text-white/90 mt-1 break-words">{error}</p>
                  <p className="text-xs text-white/80 mt-2 md:mt-3 bg-white/10 px-3 py-2 rounded-lg inline-block break-all">
                    💡 Start backend: <code className="font-mono">uvicorn app:app --port 8000</code>
                  </p>
                </div>
              </div>
            )}
          </div>

          {/* Example Sentences */}
          <div className="bg-white/95 backdrop-blur-xl rounded-3xl shadow-2xl border border-white/50 p-6 md:p-8">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 md:w-12 md:h-12 bg-gradient-to-br from-amber-400 to-orange-500 rounded-2xl flex items-center justify-center shadow-lg flex-shrink-0">
                <Sprout className="w-5 h-5 md:w-6 md:h-6 text-white" />
              </div>
              <div>
                <h3 className="text-xl md:text-2xl font-black text-gray-800">Quick Examples</h3>
                <p className="text-xs md:text-sm text-gray-600">Click to try these sample sentences</p>
              </div>
            </div>
            
            <div className="grid sm:grid-cols-2 gap-3 md:gap-4">
              {exampleTexts.map((text, index) => (
                <button
                  key={index}
                  onClick={() => loadExample(text)}
                  disabled={loading}
                  className="text-left p-4 md:p-6 bg-gradient-to-br from-white to-gray-50 hover:from-emerald-50 hover:to-green-50 border-2 border-gray-200 hover:border-emerald-400 rounded-2xl transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl hover:scale-105 group"
                >
                  <div className="flex items-start gap-3 md:gap-4">
                    <div className="flex-shrink-0 w-8 h-8 md:w-10 md:h-10 bg-gradient-to-br from-emerald-500 to-teal-500 text-white rounded-xl flex items-center justify-center font-black text-sm md:text-base shadow-lg group-hover:scale-110 transition-transform">
                      {index + 1}
                    </div>
                    <p className="text-xs md:text-sm text-gray-700 flex-1 leading-relaxed group-hover:text-gray-900 font-medium">
                      {text}
                    </p>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Footer */}
          <div className="text-center mt-8 md:mt-10 space-y-3">
            <div className="inline-block bg-white/10 backdrop-blur-xl rounded-2xl px-6 md:px-8 py-3 md:py-4 border border-white/20">
              <p className="text-white font-bold text-xs md:text-sm flex items-center gap-2 justify-center flex-wrap">
                <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
                <span>Powered by Marian NMT + Rule-based Correction</span>
              </p>
              <p className="text-emerald-200 text-xs mt-2">
                Backend: <code className="bg-white/20 px-2 py-1 rounded font-mono break-all">localhost:8000</code>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
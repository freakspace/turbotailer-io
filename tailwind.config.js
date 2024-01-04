/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: [
      './turbotailer/templates/**/*.{html,css,js}'
    ],
    safelist: [
      'lg:col-span-1',
      'lg:col-span-2',
      'lg:col-span-3',
      'form-input',
      'rounded-xl',
      'bg-black/5',
      'border-2',
      'border-white/50',
      'shadow-lg',
      'placeholder-white',
      'text-white',
      'w-full'
    ],
    theme: {
      container: {
        center: true,
        padding: '1rem',
      },
      extend: {
        colors: {
          'customBeige': '#F2F0EB',
          'customBeigeLight': '#F8F7F4',
        },
      },
      fontFamily: {
        sans: ['"GeneralSans"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography", require("@tailwindcss/line-clamp")),
    ],
  }

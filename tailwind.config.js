/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: [
      './turbotailer/templates/**/*.{html,css,js}'
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
        fontFamily: {
          sans: ['"GeneralSans"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
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

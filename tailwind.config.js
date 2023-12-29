/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: [
      './turbotailer/templates/**/*.{html,css,js}'
    ],
    theme: {
      extend: {
        colors: {
          'customBeige': '#F2F0EB',
          'customBeigeLight': '#F8F7F4',
        },
      },
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography", require("@tailwindcss/line-clamp")),
    ],
  }

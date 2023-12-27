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
        },
      },
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography", require("@tailwindcss/line-clamp")),
    ],
  }

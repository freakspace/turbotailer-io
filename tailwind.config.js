/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: [
      './turbotailer/templates/*.html', './turbotailer/templates/**/*.html'
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography", require("@tailwindcss/line-clamp")),
    ],
  }

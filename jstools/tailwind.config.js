module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },

  content: [
    '../**/templates/*.html',
    '../**/templates/**/*.html'
  ],
  theme: {
  },
  variants: {},
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

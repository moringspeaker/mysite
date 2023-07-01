const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000', // Replace with your Django backend URL
        ws: true,
        changeOrigin: true
      }
    }
  },
  // chainWebpack: config => {
  //   config.module
  //       .rule('md')
  //       .test(/\.md$/)
  //       .use('raw-loader')
  //       .loader('raw-loader')
  //       .end()
  // }
})


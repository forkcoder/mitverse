module.exports = {
  // Other configuration options...

  distDir: 'build', // Specify the directory where Next.js build output will be stored

  generateBuildId: async () => {
    // Generate a unique build ID if needed
    return 'your-unique-build-id';
  },

  publicRuntimeConfig: {
    basePath: '', // Set the base path to an empty string
  },

  serverRuntimeConfig: {
    basePath: '/', // Set the base path to an empty string
  },

  async rewrites() {
    return [
      // Rewrite requests for the root URL to the index.html file
      {
        source: '/',
        destination: '/index.html',
      },
    ];
  },
};
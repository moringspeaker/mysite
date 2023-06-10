<template>
  <Particles id="tsparticles" :options="options" />
</template>

<script>
import { Particles } from 'particles.vue3';

export default {
  name: 'App',
  components: {
    Particles,

},
  mounted() {
    const options = {options:{
        fullScreen: {
          enable: true,
          zIndex :-1,
        },
        particles: {
          links: {
            enable: true,
          },
          move: {
            enable: true,
          }
        }
      }
      // your options here...
    };
    return {
      options,
    }

  },
};
</script>
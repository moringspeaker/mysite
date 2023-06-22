<template>
    <div class="audio-player" @click="togglePlay">
      <p>Hello World!</p>
      <div class="progress-bar" :style="{ width: progress + '%' }">hi</div>
    </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";
import img from  "@/static/audio.png";
export default {
  names:"AudioPlayer",
  data(){
    return{
      bg:img,
    }
  },
  setup() {
    const audio = ref(null);
    const playing = ref(false);
    const progress = ref(0);

    const togglePlay = () => {
      if (playing.value) {
        audio.value.pause();
      } else {
        audio.value.play();
      }
      playing.value = !playing.value;
    };

    const updateProgress = () => {
      progress.value = (audio.value.currentTime / audio.value.duration) * 100;
    };

    onMounted(() => {
      audio.value = new Audio("your-audio-file.mp3");
      audio.value.addEventListener("timeupdate", updateProgress);
    });

    onUnmounted(() => {
      audio.value.removeEventListener("timeupdate", updateProgress);
      audio.value = null;
    });

    return { togglePlay, progress };
  },
};
</script>
Lastly, apply your style to your audio player in style part:

css
Copy code
<style scoped>
.audio-player {
  width: 300px; /* Customize your length */
  height: 50px;
  background: url("@/static/audio.png") no-repeat center; /* Customize your background image */
  background-size: cover;
  cursor: pointer;
}

.progress-bar {
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}
</style>

<template>
  <div class="player">
    <h2 class="player-title">{{ currentSong.name }}</h2>
    <audio controls :src="currentSong.src" @timeupdate="updateCurrentTime" ref="audioRef"></audio>
<!--    <div class="lyrics">-->
<!--      <p>{{ currentSong.lyrics }}</p>-->
<!--    </div>-->
    <div class="playlist">
      <div
          v-for="(song, index) in songs"
          :key="index"
          @click="playSong(index)"
      >
       <p class="song-name"> {{ song.name }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import SAT from '@/static/songs/Ania-Sound-of-Silence.mp3'
export default {
  name:"AudioPlayer",
  data() {
    return {
      songs: [
        { name: 'Sound of the Silence', src: SAT}
        // Add more songs as needed
      ],
      currentSong: {},
      currentTime: 0
    }
  },
  mounted() {
    // Set the first song as the current song on initial load
    this.currentSong = this.songs[0];
  },
  methods: {
    playSong(index) {
      this.currentSong = this.songs[index];
      this.$refs.audioRef.load();
      this.$refs.audioRef.play();
    },
    updateCurrentTime() {
      this.currentTime = this.$refs.audioRef.currentTime;
      // Here you could handle the display of time-stamped lyrics based on this.currentTime
    }
  }
}
</script>

<style scoped>

.player{
  grid-row: 3/4;
  grid-column: 2/3;
  background-color: #f0f0f0;
}
.player-title{
  text-align: center;
}
.song-name{
  text-align: center;
}
</style>
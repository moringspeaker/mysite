<template>
  <div class="player">
    <h2>{{ currentSong.name }}</h2>
    <audio controls :src="currentSong.src" @timeupdate="updateCurrentTime" ref="audioRef"></audio>
    <div class="lyrics">
      <p>{{ currentSong.lyrics }}</p>
    </div>
    <div class="playlist">
      <div
          v-for="(song, index) in songs"
          :key="index"
          @click="playSong(index)"
      >
        {{ song.name }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:"AudioPlayer",
  data() {
    return {
      songs: [
        { name: 'Song 1', src: 'path-to-song-1.mp3', lyrics: 'Lyrics for song 1' },
        { name: 'Song 2', src: 'path-to-song-2.mp3', lyrics: 'Lyrics for song 2' },
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
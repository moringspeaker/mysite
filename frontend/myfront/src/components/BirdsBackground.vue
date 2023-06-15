
<template>
  <div class="vanta_area" ref="Area">
    <slot>

    </slot>
  </div>
</template>


<script setup>
import * as THREE from 'three'
import BIRDS from 'vanta/src/vanta.birds'
import {onMounted,onBeforeUnmount,ref} from 'vue'

const Area=ref(null)

let vantaEffect=null;

onMounted(()=>{
  vantaEffect=BIRDS({
    el:Area.value,
    THREE:THREE,
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    backgroundColor: 0xf000000,
    color1: 0xff9700,
    color2: 0xfc0afc,
    birdSize: 0.70,
    wingSpan: 23.00,
    speedLimit: 6.00,
    separation: 34.00,
    alignment: 61.00,
    cohesion: 36.00,
    quantity: 4.00,
    backgroundAlpha: 0.9
  })
})

onBeforeUnmount(()=>{
  if(vantaEffect){
    vantaEffect.destroy()
  }
})
</script>
<style lang="less" scoped>
.vanta_area {
  width:100%;
  height:300vh;
}
</style>

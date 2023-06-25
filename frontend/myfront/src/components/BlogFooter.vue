<template>
  <div v-if="showWechatQR">
    <img :src="wechatcode" alt="WeChat QR Code" class="begge" />
  </div>
  <div v-if="showPaypalQR">
    <img :src="paypalcode" alt="PayPal QR Code"  class="begge"/>
  </div>
  <div class="footer">
    <ul class="footer-links">
      <li class="footer-link">
        <a href="mailto:chenyugu0630@outlook.com">
          <img :src="emailicon" alt="Email" />
          <span>Contact Me</span>
        </a>
      </li>
      <li class="footer-link">
        <a href="https://github.com/moringspeaker" target="_blank">
          <img :src="githubicon" alt="Github" />
          <span>My Github</span>
        </a>
      </li>
      <li class="footer-link">
        <img :src="wechaticon" alt="WeChat" @click="toggleWechatQR" />
        <span>请作者喝可乐</span>
      </li>
      <li class="footer-link">
        <img :src="paypalicon" alt="PayPal" @click="togglePaypalQR" />
        <span>Buy the author a coffee</span>

      </li>
    </ul>
  </div>
</template>

<script>

import email from '@/assets/blogfooter/icons8-email-50.png';
import github from '@/assets/blogfooter/icons8-github-50.png';
import wechat from '@/assets/blogfooter/icons8-wechat-50.png';
import paypal from '@/assets/blogfooter/icons8-paypal-50.png';

import wechatcode from '@/assets/QRcode/wechat_code.png';
import paypalcode from '@/assets/QRcode/paypa.l_code.png';
export default {
  name:'BlogFooter',
  data() {
    return {
      showWechatQR: false,
      showPaypalQR: false,
      emailicon: email,
      githubicon: github,
      wechaticon: wechat,
      paypalicon: paypal,
      wechatcode: wechatcode,
      paypalcode: paypalcode,
    }
  },
  methods: {
    toggleWechatQR() {
      this.showWechatQR = !this.showWechatQR;
      this.showPaypalQR = false;
    },
    togglePaypalQR() {
      this.showPaypalQR = !this.showPaypalQR;
      this.showWechatQR = false;
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
.footer {
  padding: 20px;
  background: #333;
  color: #fff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
  align-items: stretch;
}

.footer-links {
  list-style: none;
  display: flex;
  gap: 8vh;
}

.footer-link img {
  width: 2rem;
  height: 2rem;
  cursor: pointer;
}
.begge{
  height: 200px;
  width: 200px;
}
span{
  margin-left: 10px;
}
</style>

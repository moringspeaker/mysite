 <template>
    <div class="main-container">

    </div>
  </template>

  <script>
    import placeholder from '@/static/placeholder.png';

    import bg1 from '@/static/blog-box/p1.png';
    import bg2 from '@/static/blog-box/p2.png';
    import bg3 from '@/static/blog-box/p3.png';
    import bg4 from '@/static/blog-box/p4.png';
    import bg5 from '@/static/blog-box/p5.png';
    export default {
      name:"BlogCategory",

      props: {
        lang: {
          type: String,
          default: "EN",
        },
        blogdata: {
          type: Object, // Update the type to Array
          default: function () {
            return {}; // Set the default value to an empty array
          },
        },
      },

      data() {
        return {
          placeholder: placeholder,
          // Remove the 'blogs' data property since it's now received as a prop
          bgs:[bg1,bg2,bg3,bg4,bg5],
          blogList:[],
        };
      },

      async mounted() {
        this.blogList = Object.values(this.blogdata);
      },

      methods: {
        getImageUrl(imageSrc) {
          // Modify the image source URL here
          console.log(`http://127.0.0.1:8000${imageSrc}`);
          return `http://127.0.0.1:8000${imageSrc}`;
        },
        getBackgroundStyle(blog, index) {
          return {
            backgroundImage: `url(${this.bgs[index]})`,
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
            backgroundSize: 'cover',
          }
        },
      },
    }
  </script>

  <style scoped >

  </style>


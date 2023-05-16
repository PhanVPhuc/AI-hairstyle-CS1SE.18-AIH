<template>
    <div class="flex flex-col gap-3">
      <div v-for="i in counter.list_post_home"  class="flex flex-col gap-3 w-full h-full bg-white rounded px-4 py-4 ">
        <div class="flex justify-between relative">
            <div class="flex gap-2 items-center  ">
                <img :src="counter.domain_Backend+i.user.user_Member.Avatar" class="w-[45px] h-[45px] rounded-full"/>
                <div class="flex flex-col justify-center text-[16px] font-bold">
                    <h1>{{ i.user.username }}</h1>
                    <h1 class="text-[13px] font-medium text-gray-400">{{ i.Creation_time.split('T')[0] }}</h1>
                </div>
            </div>
        </div>
        <p class="whitespace-pre-line text-[14px] font-normal" >{{ i.Content }}</p>
        <div :class="{'grid grid-cols-1':i.post_image.length==1,
                    'grid grid-cols-2':i.post_image.length==2,
                    'grid grid-cols-3':i.post_image.length==3,
                    'grid grid-cols-4':i.post_image.length==4,
                    'grid grid-cols-5':i.post_image.length>4,
                                                                }"  class="w-full grid  gap-1">
            <img v-for="j in i.post_image" :src="counter.domain_Backend+j.Image_post" v-on:click="inset_image(i.post_image); url_image_inset_one=j.Image_post;  counter.show_image_inset=1"  class="w-full h-full border-[1px] border-gray-200"/>
            <!-- bang hien anh ///////////////////////////////////////////////////// -->
            <div v-show="counter.show_image_inset==1"  class="bg-gray-300  fixed inset-0 mt-[68px] z-50 flex flex-col justify-end cursor-pointer">
              <div v-on:click="counter.show_image_inset=0" class="w-full flex justify-end px-3 py-3"><font-awesome-icon icon="fa-solid fa-xmark" class="text-[30px]"/></div>
              <div class="flex  grow w-full justify-center items-center ">
                <img  :src="counter.domain_Backend+url_image_inset_one"  class=" max-h-[500px]  border-[1px] border-gray-200 "/>
              </div>
              <div class="flex bg-gray-400 h-[200px] w-full justify-center items-center gap-3 overflow-x-auto">
                <img v-for="v in url_image_inset" :src="counter.domain_Backend+v.Image_post" v-on:click="inset_image_one(v.Image_post)" v-bind:class="{'border-[5px] border-lime-500':url_image_inset_one==v.Image_post}"  class=" max-h-[150px]  border-[1px] border-gray-200 "/>
              </div>
            </div>
        </div>
        <!-- viet cau bl -->
        <div class="flex gap-1 w-full ">
          <img :src="counter.domain_Backend+counter.Profile.Avatar" class="w-[32px] h-[32px] rounded-full"/>
          <input type="text" placeholder="Write the answer..." v-model="i.body" @keyup.enter="add_cm(i.id,i.body)"  class="bg-gray-200 px-2 py-1 rounded-full text-[13px] grow outline-none h-[32px]"/>
        </div>
        <!-- nut xem tat ca bl -->
        <h1 v-on:click="all_cm(i.id);" class="text-[14px] font-semibold cursor-pointer">Xem tất cả bình luận</h1>
        <!-- bình luan cua moi ngươi -->
        <div v-show="counter.all_comments==i.id" class="flex flex-col gap-2">
            <div v-for="k in i.comments_post " class="flex gap-1">
              <img :src="counter.domain_Backend+k.name.user_Member.Avatar" class="w-[32px] h-[32px] rounded-full"/>
              <div class="flex flex-col gap-2">
                <div class="flex flex-col bg-gray-200 rounded px-2 py-1 max-w-full">
                  <h1 class="text-[14px] font-semibold">{{ k.name.username }}</h1>
                  <p class="text-[13px] whitespace-pre-line">{{ k.body }}</p>
                </div>
                <div v-show="k.body_admin!=null && k.body_admin!=''" class="flex gap-1">
                  <div class="border-l-[1px] border-b-[1px] border-gray-400 rounded-bl w-[10px] h-[14px]"></div>
                  <div class="w-[26px] h-[26px] rounded-full bg-lime-500 font-bold text-[18px] flex justify-center items-center">A</div>
                  <div class="flex flex-col bg-gray-200 rounded px-2 py-1 max-w-full">
                    <h1 class="text-[14px] font-semibold text-lime-600">Admin</h1>
                    <p class="text-[13px] whitespace-pre-line">{{ k.body_admin }}</p>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'


export default {
    data() {
    return {
        url_image: [],
        url_image_inset:[{ "id": 4, "Image_post": "", "post": 4 }],
        url_image_inset_one:'',
    };
    },
    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
      this.counter.List_post_home();
      this.counter.Information_Member();
    },
    methods:{
      all_cm(aa){
        if(this.counter.all_comments!=aa){this.counter.all_comments=aa}
        else{this.counter.all_comments=0};
      },
      async add_cm(aa,bb){
        await this.counter.Add_comment(aa, bb);
        bb='';
        this.counter.List_post_home();
        this.counter.all_comments=aa;
      },
      inset_image(aa){
        this.url_image_inset = aa;
        // this.url_image_inset_one = this.url_image_inset[0].Image_post;
      },
      inset_image_one(aa){
        this.url_image_inset_one = aa;
      }
    },
    components: {
    }
}
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 5px;
  height: 8px;               /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #393636;        /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #595857;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
    background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}

#cjss1::-webkit-scrollbar {
  width: 5px;
  height: 8px;               /* Chiều rộng vùng chứa scrollbar */
}
#cjss1::-webkit-scrollbar-track {
  background: #393636;        /* Màu nền ngoài của thanh scrollbar */
}
#cjss1::-webkit-scrollbar-thumb {
  background-color: #595857;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss1::-webkit-scrollbar-thumb:hover {
    background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}

#video
{
    transform: rotateY(180deg);
    -webkit-transform:rotateY(180deg); /* Safari and Chrome */
    -moz-transform:rotateY(180deg); /* Firefox */
}
</style>



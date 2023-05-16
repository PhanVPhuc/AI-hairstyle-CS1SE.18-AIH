<template>
    <div class=" flex  flex-col max-w-[300px]  min-w-[300px] h-full shrink-0  grow   mt-4  px-3 py-3 bg-gray-100 rounded ">
        <router-link to="/Profile" class="flex gap-3 items-center text-[14px] font-semibold py-2 ">
            <img :src="counter.domain_Backend+counter.Profile.Avatar" class="bg-sky-600 w-[40px] h-[40px] rounded-full " />
            <h1>{{ counter.openthongtincanhan.username }}</h1>
        </router-link>
        <router-link to="/" :class="{'bg-gray-300':counter.Path_Route.path=='/'}" class="flex gap-3 items-center text-[14px] font-semibold cursor-pointer h-[50px] px-2 rounded">
            <img src="@/assets/4.png" class="w-[25px] mr-[10px] ml-[3px]" />
            <h1>Trang chủ</h1>
        </router-link>
        <router-link to="/Profile" :class="{'bg-gray-300':counter.Path_Route.path=='/Profile'}" class="flex  items-center text-[14px] font-semibold cursor-pointer h-[50px] px-2 rounded">
            <img src="@/assets/3.png" class=" w-[28px] mr-[18px] ml-[3px] " />
            <h1>Hồ sơ</h1>
        </router-link>
    </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'


export default {

    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        // this.counter.List_un_follow();
    },
    // destroyed () {
    // document.body.classList.remove('overflow-hidden')
    // },
    methods: {
        
    }
}
</script>

<!-- <style v-if="counter.Open_Scroll==2">
  body {
   overflow: default;
  }
</style> -->

<!-- <style v-if="true">
  body {
   overflow: hidden;
  }
</style> -->
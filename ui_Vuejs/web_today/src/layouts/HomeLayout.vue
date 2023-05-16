<template>
  <div class="flex flex-col bg-gray-700 min-h-screen h-full min-w-screen w-full  items-center pt-[68px]">
    <top-ter />
    <div class="flex fixed z-40 top-[68px] gap-4 bg-gray-200 w-full h-full grow justify-center">
      <hea-der />
      <div class="w-[680px] "></div>
      <foo-ter />
      <!-- ui login and sigup -->
      <div v-if="counter.Table_Lg_Rg == 1"
        class="absolute z-30 flex flex-col inset-0 bg-gray-200 bg-[url('@/assets/bmm.png')] justify-center items-center ">
        <div v-if="counter.Form_Lg_R == true" class="flex flex-col justify-center items-center gap-2">
          <h1 class=" text-[25px] text-gray-700 font-semibold mb-3">Đăng nhập</h1>
          <input placeholder="Tên tài khoản" v-model="counter.Lg.username"
            class="px-3 rounded w-[480px] h-[48px] drop-shadow-md" />
          <input type="password" placeholder="Mật khẩu" v-model="counter.Lg.password"
            class="px-3 rounded w-[480px] h-[48px] drop-shadow-md" />
          <button v-on:click="counter.dangnhaptaikhoanvataocookie();"
            class="rounded drop-shadow-md w-[480px] h-[48px] bg-gradient-to-t from-[#f87171] to-[#ec4899] text-[18px] text-white font-semibold">Đăng
            nhập</button>
          <h1 v-on:click="counter.Form_Lg_R = !counter.Form_Lg_R"
            class=" text-[16px] text-gray-600 font-medium mb-3 cursor-pointer">Không có tài khoản ? Đăng ký ngay</h1>
        </div>
        <div v-if="counter.Form_Lg_R == false" class="flex flex-col justify-center items-center gap-2">
          <h1 class=" text-[25px] text-gray-700 font-semibold mb-3">Đăng kí</h1>
          <input placeholder="Tên tài khoản" v-model="counter.Rg.username"
            class="px-3 rounded w-[480px] h-[48px] drop-shadow-md " />
          <input placeholder="Email" v-model="counter.Rg.email" class="px-3 rounded w-[480px] h-[48px] drop-shadow-md" />
          <input type="password" placeholder="Mật khẩu" v-model="counter.Rg.password"
            class="px-3 rounded w-[480px] h-[48px] drop-shadow-md" />
          <input type="password" placeholder="Xác nhận lại mật khẩu" v-model="counter.Rg.confirm_password"
            class="px-3 rounded w-[480px] h-[48px] drop-shadow-md" />
          <h1 v-if="counter.Rg_TC == 2" class="text-lime-600 font-bold text-[20px]">{{ counter.Error_Rg.thong_bao }}</h1>
          <h1 v-if="counter.Error_Rg.so == 2" class="text-red-600 font-bold text-[20px]">{{ counter.Error_Rg.thong_bao }}
          </h1>
          <button v-on:click="counter.dangkitaikhoan();"
            class="rounded drop-shadow-md w-[480px] h-[48px] bg-gradient-to-t from-[#f87171] to-[#ec4899] text-[18px] text-white font-semibold">Đăng
            kí</button>
          <h1 v-on:click="counter.Form_Lg_R = !counter.Form_Lg_R"
            class=" text-[16px] text-gray-600 font-medium mb-3 cursor-pointer">Bạn đã có tài khoản ? Đăng nhập ngay bây
            giờ</h1>
        </div>
      </div>
    </div>
    <router-view v-if="counter.Table_Lg_Rg == 2" id="slider2"
      class=" absolute z-40  w-[680px] top-[68px] mt-4 pb-3 mx-auto  " />
  </div>
</template>
  

<script>
// Import thành phần (components) NavBar, SideBar, FooterBar để sử dụng
import HeaDer from '@/components/HeaDer.vue'
import FooTer from '@/components/FooTer.vue'
import TopTer from '@/components/TopTer.vue'

import { useCounterStore } from '@/stores/counter';


// Để sử dụng được các thẻ (tag) của các component tương ứng
// <nav-bar />     -> component NavBar
// <side-bar />    -> component SideBar
// <footer-bar />  -> component FooterBar
// Chúng ta phải khai báo trong thuộc tính `components` của phần export default {}
export default {
  setup() {
    const counter = useCounterStore();
    return { counter }
  },
  mounted: function () {
    this.counter.keep_login();
  },
  methods: {
  },
  components: {
    HeaDer,
    FooTer,
    TopTer,
  }
}
</script>
  
<style>
body::-webkit-scrollbar {
  width: 14px;
  /* Chiều rộng vùng chứa scrollbar */
}

body::-webkit-scrollbar-track {
  background: #E5E7EB;
  /* Màu nền ngoài của thanh scrollbar */
}

body::-webkit-scrollbar-thumb {
  background-color: #bcbcbc;
  /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;
  /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}

body::-webkit-scrollbar-thumb:hover {
  background-color: #bcbcbc;
  /* Hiệu ứng di chuột đổi màu*/
}

#slider2::-webkit-scrollbar {
  width: 6px;
  /* Chiều rộng vùng chứa scrollbar */
}

#slider2::-webkit-scrollbar-track {
  background: #F3F4F6;
  /* Màu nền ngoài của thanh scrollbar */
}

#slider2::-webkit-scrollbar-thumb {
  background-color: v-bind(cvb);
  /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;
  /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}</style>

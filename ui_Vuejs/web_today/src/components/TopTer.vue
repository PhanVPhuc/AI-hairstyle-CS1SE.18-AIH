<template>
    <div  class="flex fixed top-0 z-50 w-full h-[68px] bg-white items-center justify-between drop-shadow-md px-4">
        <div class="flex gap-2 items-center text-[25px] font-bold">
            <router-link to='/'><img src="@/assets/th.png" class="w-[50px] h-[50px]"/></router-link>
            <h1 v-if="counter.Table_Lg_Rg==1">Shop Hair</h1>
            <div v-if="counter.Table_Lg_Rg==2" class="flex  bg-gray-200 h-[40px] gap-3 items-center w-[364px] rounded-full px-3">
                <router-link to="/Search-Friends" v-on:click="counter.Search_friend();">
                    <button><svg   role="img" height="24" width="24" aria-hidden="true" class="fill-gray-900 Svg-sc-ytk21e-0 uPxdw mOLTJ2mxkzHJj6Y9_na cursor-pointer_" viewBox="0 0 24 24" data-encore-id="icon"><path d="M10.533 1.279c-5.18 0-9.407 4.14-9.407 9.279s4.226 9.279 9.407 9.279c2.234 0 4.29-.77 5.907-2.058l4.353 4.353a1 1 0 1 0 1.414-1.414l-4.344-4.344a9.157 9.157 0 0 0 2.077-5.816c0-5.14-4.226-9.28-9.407-9.28zm-7.407 9.279c0-4.006 3.302-7.28 7.407-7.28s7.407 3.274 7.407 7.28-3.302 7.279-7.407 7.279-7.407-3.273-7.407-7.28z"></path></svg></button>
                </router-link>
                <input placeholder="Search..."  class="w-full text-gray-600  text-[16px] font-normal bg-gray-200 outline-none" v-model="counter.search_friend"/>
            </div>
        </div>

        <img :src="counter.domain_Backend+counter.Profile.Avatar" v-if="counter.Table_Lg_Rg == 2" v-on:click="counter. Show_DD_image=!counter. Show_DD_image" class="bg-sky-600 w-[50px] h-[50px] rounded-full cursor-pointer" />

        <div v-if="counter.Table_Lg_Rg == 1">
            <button v-if="counter.Form_Lg_R==false" v-on:click="counter.Form_Lg_R=!counter.Form_Lg_R" class="drop-shadow-md w-[90px] py-2 text-[16px] text-semibold bg-black rounded text-white">Đăng nhập</button>
            <button v-if="counter.Form_Lg_R==true" v-on:click="counter.Form_Lg_R=!counter.Form_Lg_R" class="drop-shadow-md w-[90px] py-2 text-[16px] text-semibold bg-black rounded text-white">Đăng kí</button>
        </div>
    </div>
    <div v-show="counter. Show_DD_image==true && counter.Table_Lg_Rg == 2 " v-on:click="counter.dangxuattaikhoan(); counter. Show_DD_image=!counter. Show_DD_image" class="flex fixed z-50 right-4 top-[68px] drop-shadow-md  bg-white cursor-pointer rounded   gap-3 items-center text-[16px] font-semibold w-[150px] h-[40px] px-2">
        <i data-visualcompletion="css-img" class="x1b0d499 xep6ejk" style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/yk/r/lMvzx5fIZmt.png&quot;); background-position: 0px -364px; background-size: auto; width: 20px; height: 20px; background-repeat: no-repeat; display: inline-block;"></i>
        <router-link to="/">Đăng xuất</router-link>
    </div>
</template>


<script >

    import { useCounterStore } from '@/stores/counter';
    import axios from 'axios';
    import VueCookies from 'vue-cookies'


    export default {

    setup() {
        const counter = useCounterStore();
        return {counter}
    },
    mounted: function () {
        // src="https://cse.google.com/cse.js?cx=55c97eef5881f4231"
    },
    }
</script>



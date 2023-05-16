<template>
    <div class="flex flex-col rounded gap-3">
        <div class="flex flex-col w-full bg-white rounded px-4 py-4">
            <div class="flex gap-5 items-center ">
                <div class="flex justify-center items-center relative w-[200px] h-[200px]">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="min-w-[200px] h-[200px] rounded-full"/>
                    <!-- <div class=" absolute bottom-2 right-2 w-[45px] h-[45px] cursor-pointer ">
                        <div class="relative bg-gray-200  w-[45px] h-[45px] rounded-full "></div>
                        <font-awesome-icon icon="fa-solid fa-camera" class="absolute inset-0 mx-auto my-auto text-[25px] text-gray-800"/>
                    </div> -->
                </div>
                <div class="flex flex-col justify-center text-[30px] font-bold">
                    <h1>{{ counter.openthongtincanhan.username }}</h1>
                    <!-- <h1 class="text-[16px] font-medium shrink-0 whitespace-nowrap">{{ counter.list_followed.length }} Follow</h1> -->
                    <div class="flex gap-2 mt-2">
                        <!-- <img v-for=" i in counter.list_followed.slice(0,counter.SL_F)" :src="counter.domain_Backend+i.user[0].user_Member.Avatar" class="w-[40px] h-[40px] rounded-full"/> -->
                    </div>
                </div>
                <div class="flex flex-col gap-3 w-full grow justify-center items-center">
                    <div class="flex flex-col gap-2">
                        <div v-show="counter.Profile.Address!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-house-chimney" class="text-[18px]" /><h1 class="font-medium">Live in {{counter.Profile.Address}}</h1></div>
                        <div v-show="counter.Profile.Date_of_birth!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-cake-candles" class="text-[18px]" /><h1 class="font-medium">{{counter.Profile.Date_of_birth}}</h1></div>
                        <div v-show="counter.Profile.Phone_number!='null' && counter.Profile.Phone_number!=''" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-square-phone" class="text-[20px]" /><h1 class="font-medium">{{counter.Profile.Phone_number}}</h1></div>
                        <div class="flex gap-2 items-center "><font-awesome-icon icon="fa-solid fa-envelope" class="text-[20px]" /><h1 class="flex mb-1 font-medium">{{counter.openthongtincanhan.email}}</h1></div>
                    </div>
                </div>
            </div>
            <div class="flex  gap-3 mt-4 w-full grow ">
                <button v-on:click="counter.Edit_Post.so=2;" class="flex items-center justify-center gap-1 font-semibold w-[150px] py-1 rounded bg-sky-500"><font-awesome-icon icon="fa-solid fa-plus" /><h1 class="">Thêm bài đăng</h1></button>
                <button v-on:click="counter.Edit_Profile.so=2; counter.Edit_Profile.Address = counter.Profile.Address; counter.Edit_Profile.Date_of_birth = counter.Profile.Date_of_birth;" class="flex items-center justify-center gap-1 font-semibold w-[190px] py-1 rounded bg-sky-500"><font-awesome-icon icon="fa-solid fa-pen" /><h1 class="whitespace-nowrap">Chỉnh sửa thông tin</h1></button>
                <button v-on:click="counter.Hair=2" class="flex items-center justify-center gap-1 font-semibold w-[170px] py-1 rounded bg-sky-500"><font-awesome-icon icon="fa-solid fa-image" class="mt-[2px]" /><h1 class="">Mẫu tóc đã chọn</h1></button>
                <button v-on:click="counter.Scan_Hair=2"  class="flex items-center justify-center gap-1 font-semibold w-[120px] py-1 rounded bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"><font-awesome-icon icon="fa-solid fa-camera-rotate" class="text-[20px]"/><h1 class="">Face scan</h1></button>
            </div>

            <!-- bang edit profile -->
            <div v-show="counter.Edit_Profile.so==2" v-on:click="counter.Edit_Profile.so=1" class="bg-gray-300 rounded fixed inset-0 z-40 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Edit_Profile.so==2" class="bg-white rounded fixed inset-0 z-50 mx-auto my-auto w-[300px] h-[430px] flex flex-col justify-between items-center px-3 py-3">
                <h1 class="text-[22px] font-semibold border-b-[1px] border-gray-200 w-full text-center pb-3">Chỉnh sửa thông tin</h1>
                <div class="flex justify-center items-center relative w-[200px] h-[200px]">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="min-w-[200px] h-[200px] rounded-full"/>
                    <label for="file" class=" absolute bottom-2 right-2 w-[45px] h-[45px] cursor-pointer ">
                        <div class="relative bg-gray-200  w-[45px] h-[45px] rounded-full "></div>
                        <font-awesome-icon icon="fa-solid fa-camera" class="absolute inset-0 mx-auto my-auto text-[25px] text-gray-800"/>
                        <input type="file" accept="image/*"  id="file" ref="file" class="hidden" v-on:change="Update_Member();"/>
                    </label>
                </div>
                <div class="flex flex-col gap-2">
                    <div class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-house-chimney" class="text-[18px]" /><input v-model="counter.Edit_Profile.Address" class="font-medium flex items-center outline-none bg-gray-100 px-2 py-1 rounded" /></div>
                    <div class="flex gap-2 items-center ml-1"><font-awesome-icon icon="fa-solid fa-cake-candles" class="text-[18px]" /><input v-model="counter.Edit_Profile.Date_of_birth" class="font-medium flex items-center outline-none bg-gray-100 px-2 py-1 rounded" /></div>
                    <div class="flex gap-2 items-center ml-1"><font-awesome-icon icon="fa-solid fa-square-phone"  class="text-[20px]" /><input v-model="counter.Edit_Profile.Phone_number" class="font-medium flex items-center outline-none bg-gray-100 px-2 py-1 rounded" /></div>
                </div>
                <button v-on:click=" Update_Member_path(); counter.Edit_Profile.so=1;" class="flex items-center justify-center gap-1 font-semibold w-[90px] py-1 rounded bg-sky-500"><h1 class="">Cập nhật</h1></button>
            </div>

            <!-- bang add post -->
            <div v-show="counter.Edit_Post.so==2" v-on:click="counter.Edit_Post.so=1;" class="bg-gray-300 rounded fixed z-40 inset-0 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Edit_Post.so==2" class="bg-white rounded fixed z-50 inset-0 mx-auto my-auto w-[450px] h-[550px] flex flex-col justify-between items-center px-3 gap-3 py-3">
                <h1 class="text-[22px] font-semibold border-b-[1px] border-gray-200 w-full text-center pb-3">Chỉnh sửa bài đăng</h1>
                <div class="flex gap-3 items-center text-[14px] font-semibold w-full">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="bg-sky-600 w-[40px] h-[40px] rounded-full" />
                    <h1>{{ counter.openthongtincanhan.username }}</h1>
                </div>
                <textarea v-model="counter.Create_Post.Content" placeholder="Bạn đang nghĩ gì ?" id="slider3" class="w-full min-h-[100px] text-[12px] font-normal outline-none"></textarea>
                <label for="file1" class="bg-gray-100 w-full h-[250px] relative flex justify-center items-center cursor-pointer">
                    <div v-if="url_image.length>0" id="slider3" class=" flex flex-col w-full h-full overflow-y-auto border-[1px] border-gray-200">
                        <img v-for="i in url_image" :src="i" />
                    </div>
                    <font-awesome-icon   icon="fa-solid fa-plus" v-if="url_image.length==0" class="text-[35px] text-gray-500"/>
                    <font-awesome-icon icon="fa-solid fa-circle-xmark" v-if="url_image.length>0" v-on:click="url_image=[]" class="absolute top-2 right-2 text-[22px] text-gray-400" />
                </label>
                <button v-on:click="Update_Member1(); counter.Edit_Post.so=1;" class="w-full py-2 text-[18px] font-semibold bg-sky-500 rounded">Đăng</button>
                <input type="file" accept="image/*"  id="file1" ref="file1" multiple class="hidden" @change="onFileChange();"/>
                <h1>{{ counter.examplee }}</h1>
            </div>

            <!-- bang cac loai mau toc -->
            <div v-show="counter.Hair==2" v-on:click="counter.Hair=1;" class="bg-gray-300 rounded fixed z-40 inset-0 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Hair==2" id="slider4" class="bg-white rounded fixed z-50 inset-0 mx-auto my-auto w-[550px] h-[650px] flex flex-col justify-between items-center px-3 gap-3 py-3 overflow-y-auto">
              <h1 class="flex justify-center items-center w-full text-[18px] font-semibold">Các mẫu tóc mà bạn đã từng lựa chọn</h1>
              <div class="flex flex-col justify-center items-center gap-3 w-[500px]">
                <div class="flex justify-center items-center gap-1">
                  <div class="border-b-[1px] border-gray-400  w-[208px]"></div>
                  <h1 class="font-medium text-gray-500">22/3/2026</h1>
                  <div class="border-b-[1px] border-gray-400  w-[208px]"></div>
                </div>
                <img src="https://tapchilamdep.com/wp-content/uploads/2021/06/kieu-toc-undercut-han-quoc-co-phan-toc-dinh-dau-dai.jpg" />
              </div>
              <div class="flex flex-col justify-center items-center gap-3 w-[500px]">
                <div class="flex justify-center items-center gap-1">
                  <div class="border-b-[1px] border-gray-400  w-[208px]"></div>
                  <h1 class="font-medium text-gray-500">22/3/2026</h1>
                  <div class="border-b-[1px] border-gray-400  w-[208px]"></div>
                </div>
                <img src="https://tapchilamdep.com/wp-content/uploads/2021/06/kieu-toc-undercut-han-quoc-co-phan-toc-dinh-dau-dai.jpg" />
              </div>
            </div>

            <!-- bang scan face -->
            <div v-show="counter.Scan_Hair==2" v-on:click="counter.Scan_Hair=1;" class="bg-gray-300 rounded fixed z-40 inset-0 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Scan_Hair==2"  class="bg-white rounded fixed z-50 inset-0 mx-auto my-auto w-[550px] h-[650px] flex flex-col justify-between items-center px-3 py-3 ">
              <div class="w-full h-[500px] bg-gray-400">Camera</div>
              <div class="flex justify-between w-full gap-3">
                <div class="flex flex-col gap-1 grow ">
                  <div class="flex items-center">
                    <h1 class="w-[75px] font-medium">Giới tính:</h1>
                    <input  class="font-normal flex items-center outline-none bg-gray-100 px-2 py-1 rounded grow" />
                  </div>
                  <div class="flex items-center">
                    <h1 class="w-[75px] font-medium">Màu da:</h1>
                    <input  class="font-normal flex items-center outline-none bg-gray-100 px-2 py-1 rounded grow" />
                  </div>
                  <div class="flex items-center">
                    <h1 class="w-[75px] font-medium">Màu tóc:</h1>
                    <input  class="font-normal flex items-center outline-none bg-gray-100 px-2 py-1 rounded grow" />
                  </div>
                </div>
                <button class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 w-[100px] rounded text-[18px] font-bold">Scan</button>
              </div>
            </div>
        </div>
        <div v-for="i in counter.list_user_post"  class="flex flex-col gap-3 w-full h-full bg-white rounded px-4 py-4 ">
            <div class="flex justify-between relative">
                <div class="flex gap-2 items-center  ">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="w-[45px] h-[45px] rounded-full"/>
                    <div class="flex flex-col justify-center text-[16px] font-bold">
                        <h1>{{ counter.openthongtincanhan.username }}</h1>
                        <h1 class="text-[13px] font-medium text-gray-400">{{ i.Creation_time.split('T')[0] }}</h1>
                    </div>
                </div>
                <font-awesome-icon icon="fa-solid fa-ellipsis" v-on:click="all_cm1(i.id)" class="cursor-pointer text-[18px] hover:bg-gray-200 px-2 py-2 rounded-full"/>
                <div v-show="counter.show_delete_post==i.id" class="flex justify-center items-center absolute top-6 right-5 drop-shadow-md rounded w-[100px] py-1 font-medium bg-gray-200 cursor-pointer"><h1 v-on:click="counter.Delete_Post(i.id)">Xóa bài viết</h1></div>
            </div>
            <p class="whitespace-pre-line text-[14px] font-normal" v-on:click="counter.show_delete=0">{{ i.Content }}</p>
            <div :class="{'grid grid-cols-1':i.post_image.length==1,
                        'grid grid-cols-2':i.post_image.length==2,
                        'grid grid-cols-3':i.post_image.length==3,
                        'grid grid-cols-4':i.post_image.length==4,
                        'grid grid-cols-5':i.post_image.length>4,
                                                                    }" v-on:click="counter.show_delete=0" class="w-full grid  gap-1">
                <img v-for="j in i.post_image" :src="counter.domain_Backend+j.Image_post" v-on:click="inset_image(i.post_image); url_image_inset_one=j.Image_post;  counter.show_image_inset=1" class="w-full h-full border-[1px] border-gray-200"/>
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
            <div class="flex justify-between">
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
        this.counter.Information_Member();
        this.counter.List_user_post();
    },
    methods:{
        async Update_Member() {
      let image = this.$refs.file.files[0];

      let formData = new FormData();
      formData.append('Date_of_birth', this.counter.Edit_Profile.Date_of_birth);
      formData.append('Address', this.counter.Edit_Profile.Address);
      formData.append('Phone_number', this.counter.Edit_Profile.Phone_number);
      formData.append('Avatar', image);
      formData.append('user', this.counter.openthongtincanhan.id);
      await axios({ method: 'put',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/update-information-user/' + this.counter.Profile.id + '/' });
      this.counter.Information_Member();
    },
    async Update_Member_path() {
            let formData = new FormData();
            formData.append('Date_of_birth', this.counter.Edit_Profile.Date_of_birth);
            formData.append('Address', this.counter.Edit_Profile.Address);
            formData.append('Phone_number', this.counter.Edit_Profile.Phone_number);
            formData.append('user', this.counter.openthongtincanhan.id);
            await axios({ method: 'patch',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/update-information-user/' + this.counter.Profile.id + '/' });
            this.counter.Information_Member();
    },
    async Update_Member1() {
      let formData = new FormData();

      for (var i = 0; i < this.$refs.file1.files.length; i++ ){
        let file = this.$refs.file1.files[i];
        formData.append('uploaded_images', file);
        }

      formData.append('Content', this.counter.Create_Post.Content);
      formData.append('user', this.counter.openthongtincanhan.id);

      await axios({ method: 'post',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/create-post'  });
      this.counter.List_user_post();
    },
    onFileChange(){
        for (var i = 0; i < this.$refs.file1.files.length; i++ ){
            let file = this.$refs.file1.files[i];
            this.url_image.push(URL.createObjectURL(file));
        }
    },
    all_cm11(aa,bb){
        if(this.counter.show_delete_comment!=aa){this.counter.show_delete_comment=aa}
        else{this.counter.show_delete_comment=0};
        this.counter.s_d_p=bb;
    },
    all_cm1(aa){
      if(this.counter.show_delete_post!=aa){this.counter.show_delete_post=aa}
        else{this.counter.show_delete_post=0};
    },
    all_cm(aa){
        if(this.counter.all_comments!=aa){this.counter.all_comments=aa}
        else{this.counter.all_comments=0};
      },
      async add_cm(aa,bb){
        await this.counter.Add_comment(aa, bb);
        bb='';
        this.counter.List_user_post();
        this.counter.all_comments=aa;
      },
      async delete_comment(aa){
        await this.counter.Delete_comment(aa);
        this.counter.List_user_post();
        this.counter.show_delete_comment=0;
        this.s_d_p=0;
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
#slider3::-webkit-scrollbar {
  width: 6px;               /* Chiều rộng vùng chứa scrollbar */
}
#slider3::-webkit-scrollbar-track {
  background: #F3F4F6;        /* Màu nền ngoài của thanh scrollbar */
}
#slider3::-webkit-scrollbar-thumb {
  background-color: #dbdcdf;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}

#slider4::-webkit-scrollbar {
  width: 6px;               /* Chiều rộng vùng chứa scrollbar */
}
#slider4::-webkit-scrollbar-track {
  background: #F3F4F6;        /* Màu nền ngoài của thanh scrollbar */
}
#slider4::-webkit-scrollbar-thumb {
  background-color: #dbdcdf;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}


</style>
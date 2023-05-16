import { defineStore } from 'pinia';

import axios from 'axios';
import VueCookies from 'vue-cookies'
import { fa0 } from '@fortawesome/free-solid-svg-icons';

import { useRoute } from 'vue-router';
const Route = useRoute();


export const useCounterStore = defineStore('counter', {
  state: () => {
    return {
      domain_Backend: 'http://127.0.0.1:8000', domain_Frontend: '', Path_Route: useRoute(),

      // Social///////////////////////
      Table_Lg_Rg: 0, Form_Lg_R: true, Lg: { username: '', password: '' }, Rg: { username: '', email: '', password: '', confirm_password: '' },
      openthongtincanhan: { id: '', username: '', email: '', password: '', token: '' }, Error_Lg: { so: 1, thong_bao: '' }, Error_Rg: { so: 1, thong_bao: '' }, Rg_TC: 1, Show_DD_image: false,
      Profile: { id: '', Date_of_birth: '', Address: '', Avatar: '' }, Edit_Profile: { so: 1, Date_of_birth: '', Address: '', Phone_number: '' }, Edit_Post: { so: 1, Date_of_birth: '', Address: '' }, Data_Image: '', SL_F: 0,
      Create_Post: { Content: '' }, examplee: '', list_user_post: '', show_delete: '', list_post_home: '', search_friend: '', list_search_friend: '',
      all_comments: 0, body_comment: '', show_delete_comment: 0, s_d_p: 0, show_image_inset: 0, Hair: 1, Select_Hair: 0, show_delete_post: 0, Scan_Hair: 0,

    }
  },

  getters: {
    // cookievalue: (state) => state.openthongtincanhan.token + "(Theta)" + state.openthongtincanhan.id,
  },

  actions: {
    async dangnhaptaikhoanvataocookie() {
      try {
        this.openthongtincanhan = await axios({ method: 'post', url: this.domain_Backend + '/login', data: { "username": this.Lg.username, "password": this.Lg.password } });
        this.openthongtincanhan = this.openthongtincanhan.data;
        VueCookies.set("Lg_T", this.openthongtincanhan.token + "eab42d241cad8d" + this.openthongtincanhan.id, "7d");
        this.Table_Lg_Rg = 2;
        VueCookies.set("Tab_Lg_T", 2, "365d");
        this.Information_Member();
      }
      catch (error) {
        this.Error_Lg.so = 2;
        this.Error_Lg.thong_bao = error.response.data['Error message English'];
      }

    },
    async keep_login() {
      try {
        this.openthongtincanhan.id = await VueCookies.get("Lg_T").split('eab42d241cad8d')[1];
        this.openthongtincanhan.token = await VueCookies.get("Lg_T").split('eab42d241cad8d')[0];
      }
      catch {
        this.openthongtincanhan = { id: '', username: '', email: '', password: '', token: '' };
        this.Table_Lg_Rg = 1;
      }
      if (this.openthongtincanhan.token != '') {
        try {
          // this.Table_Lg_Rg = 2;
          this.openthongtincanhan = await axios({ method: 'post', url: this.domain_Backend + '/keeplogin', data: { "id": this.openthongtincanhan.id, "token": this.openthongtincanhan.token }, headers: { Authorization: 'Token ' + this.openthongtincanhan.token } });
          this.Table_Lg_Rg = 2;
          this.openthongtincanhan = this.openthongtincanhan.data;
        }
        catch {
          this.openthongtincanhan = { id: '', username: '', email: '', password: '', token: '' };
          this.Table_Lg_Rg = 1;
        }
      }
    },
    async dangxuattaikhoan() {
      await axios({ method: 'post', url: this.domain_Backend + '/user/auth/logout/', headers: { Authorization: 'Token ' + this.openthongtincanhan.token } });
      this.Table_Lg_Rg = 1;
      VueCookies.set("Tab_Lg_T", 1, "365d");
      VueCookies.remove("Lg_T");
    },
    async dangkitaikhoan() {
      try {
        await axios({ method: 'post', url: this.domain_Backend + '/register', data: { "email": this.Rg.email, "username": this.Rg.username, "password": this.Rg.password, "confirm_password": this.Rg.confirm_password } });
        this.Rg_TC = 2;
        this.Error_Rg.so = 1;
        this.Error_Rg.thong_bao = 'Đăng ký tài khoản thành công';
        this.Rg = { username: '', email: '', password: '', confirm_password: '' };
      }
      catch (error) {
        this.Error_Rg.so = 2;
        this.Rg_TC = 1;
        this.Error_Rg.thong_bao = error.response.data['Error message English'];
      }
    },
    async Information_Member() {
      this.Profile = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/information-user' });
      this.Profile = this.Profile.data.Data;
      this.Edit_Profile.Address = this.Profile.Address;
      this.Edit_Profile.Date_of_birth = this.Profile.Date_of_birth;
      this.Edit_Profile.Phone_number = this.Profile.Phone_number;
    },
    async List_user_post() {
      this.list_user_post = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-post-user' });
      this.list_user_post = this.list_user_post.data.Data;

      // for (let i = 0; i < this.list_user_post.length; i++) {
      //   this.list_user_post[i].liked_Y_N = 'no';
      //   for (let j = 0; j < this.list_user_post[i].like.length; j++) {
      //     if (this.openthongtincanhan.username == this.list_user_post[i].like[j].username) {
      //       this.list_user_post[i].liked_Y_N = 'yes';
      //     }
      //   }
      // }
    },
    async Delete_Post(post_id) {
      await axios({ method: 'get', params: { post_id: post_id }, url: this.domain_Backend + '/delete-post' });
      this.List_user_post();
    },
    async List_post_home() {
      this.list_post_home = await axios({ method: 'get', url: this.domain_Backend + '/list-post' });
      this.list_post_home = this.list_post_home.data.Data;

      // for (let i = 0; i < this.list_post_home.length; i++) {
      //   this.list_post_home[i].liked_Y_N = 'no';
      //   for (let j = 0; j < this.list_post_home[i].like.length; j++) {
      //     if (this.openthongtincanhan.username == this.list_post_home[i].like[j].username) {
      //       this.list_post_home[i].liked_Y_N = 'yes';
      //     }
      //   }
      // }
    },
    async Add_comment(aa, bb) {
      await axios({ method: 'post', data: { username_id: this.openthongtincanhan.id, post_id: aa, body: bb }, url: this.domain_Backend + '/add-comment' });
    },
    async Delete_comment(aa) {
      await axios({ method: 'get', params: { comment_id: aa }, url: this.domain_Backend + '/delete-comment' });
    },
  }
})



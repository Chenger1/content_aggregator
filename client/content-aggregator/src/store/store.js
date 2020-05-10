import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export const store = new Vuex.Store({
    state:{
        data:{}
    },
    getters:{
        GET_DATA_FROM_STORE:(state, payload)=>{
            return state.data
        }
    },
    mutations:{
        SET_DATA:(state, payload)=>{
            state.data = payload;
        }
    },
    actions:{
        GET_DATA: (context, payload)=>{
            axios.get('http://localhost:5000')
            .then((response)=>{
                console.log(response.data)
                context.commit('SET_DATA', response.data)
            })
        }
    }
})
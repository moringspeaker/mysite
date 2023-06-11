import axios  from "axios"
// import {error} from "@babel/eslint-parser/lib/convert";

const instance = axios.create({
    // public configuration
    timeout:5000
})

// interceptors
instance.interceptors.request.use(
    config =>{
        if (config.methods === "post"){
            let params = new URLSearchParams();
            for(let key in config.data){
                params.append(key,config.data[key]);
            }
            config.data = params.toString();
        }
        return config;
    },
    error =>{
        return Promise.reject(error);
    }
)

//before receive
instance.interceptors.response.use(
    response =>{
        return response.status === 200 ? Promise.resolve(response) : Promise.reject(response);
    },
    error =>{
        const { response } =error;
        console.log(response.status);
        console.log(response.info);
    }
)

export default instance;
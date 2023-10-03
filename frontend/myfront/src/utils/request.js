import axios  from "axios"
import Cookies from 'js-cookie'; // you need to install this package using npm install js-cookie

const instance = axios.create({
    // public configuration
    withCredentials: true,
    timeout:5000,
    headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': Cookies.get('csrftoken') // get CSRF token from cookies
    }
});

// interceptors
instance.interceptors.request.use(
    config => {
        if (config.method.toUpperCase() === "POST"){
            let params = new URLSearchParams();
            for(let key in config.data){
                params.append(key,config.data[key]);
            }
            config.data = params;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

// before receive
instance.interceptors.response.use(
    response => {
        if ((response.status >= 200 && response.status < 300) || response.status === 301 || response.status === 302) {
            return Promise.resolve(response);
        } else {
            return Promise.reject(response);
        }
    },
    error => {
        const { response } =error;
        if (response) {
            console.log(response.status);
            console.log(response.info);
        }
        return Promise.reject(error);
    }
);

export default instance;

<template>
  <div class="bg-color">
    <div class="container">
      <div class="main-nav mb-5">
        <form @submit.prevent="onSubmit">
          <div class="d-flex w-50 mx-auto">
            <input
              class="form-control mr-1"
              placeholder="Search for a city"
              v-model="city_query"
            />
            <button class="btn btn-secondary">enter</button>
          </div>
        </form>
        <p class="text-center" v-if="error">{{ error }}</p>
      </div>

      <div class="container">
        <div class="">
          <div class="wrapper">
            <div v-for="info in infos">
              <div class="card" style="color: #4b515d; border-radius: 35px">
                <div class="card-body p-4">
                  <div class="d-flex">
                    <h6 class="flex-grow-1">
                      {{ info.name }}, {{ info.sys.country }}
                    </h6>
                    <h6>
                      <!-- {{ infos.lastupdate }} -->
                    </h6>
                  </div>

                  <div class="d-flex flex-column text-center mt-5 mb-4">
                    <h6
                      class="display-4 mb-2 font-weight-bold"
                      style="color: #1c2331"
                    >
                      {{ info.main.temp }} C
                    </h6>
                    <span style="color: #868b94">
                      <h6 class="mb-0">
                        <strong>{{ info.weather[0]["main"] }}</strong>
                      </h6>
                      <div class="small">
                        {{ info.weather[0]["description"] }}
                      </div>
                    </span>
                  </div>

                  <div class="d-flex align-items-center">
                    <div class="flex-grow-1" style="font-size: 1rem">
                      <div>
                        <i class="fas fa-wind fa-fw" style="color: #868b94"></i>
                        <span class="ms-1">
                          {{ (info.wind.speed * kmh).toFixed(2) }} km/h
                        </span>
                      </div>
                      <div>
                        <i class="fas fa-tint fa-fw" style="color: #868b94"></i>
                        <span class="ms-1">
                          {{ info.main.humidity }}% Humidity
                        </span>
                      </div>
                    </div>
                    <div>
                      <img
                        :src="`http://openweathermap.org/img/w/${info.weather[0]['icon']}.png`"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
export default {
  name: "HomeView",
  data() {
    return {
      city_query: null,
      infos: [],
      cities: [],
      name: {},
      kmh: 3.6,
      error: "",
    };
  },
  computed: {},
  methods: {
    async onSubmit() {
      if (!this.city_query) {
        this.error = "You can't enter an empty city";
        return;
      }
      let endpoint1 = `https://api.openweathermap.org/data/2.5/weather?q=${this.city_query}&units=metric&appid=50fa221d32e710d1045aad7ee9da01a8`;
      let endpoint2 = "/api/";

      try {
        const response1 = await axios.get(endpoint1);
        const response2 = await axios.post(endpoint2, {
          city_name: this.city_query,
        });
        this.city_query = null;
        if (this.error) {
          this.error = null;
        }
        this.infos.unshift(response1.data);
      } catch (error) {
        // console.log(error);
        if (error.response) {
          this.error = error.response.data.message;
        }
      }
    },
    // async deleteCity() {
    //   const endpoint = `/api/${this.cities.id}/`;
    //   try {
    //     await axios.delete(endpoint);
    //     this.infos.splice(this.infos.indexOf(this.cities.id), 1); //changes the contents of an array by removing or replacing existing elements and/or adding new elements in place
    //   } catch (error) {
    //     console.log(error.response);
    //   }
    // },
    // async getWeather() {
    //   let endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${this.city_query}&units=metric&appid=50fa221d32e710d1045aad7ee9da01a8`;

    //   try {
    //     const response = await axios.get(endpoint);
    //     console.log(response);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    async getPreviousWeather() {
      let endpoint = "/api/";
      let promises = [];
      try {
        const response1 = await axios.get(endpoint);

        this.cities = response1.data;
        for (let i = 0; i < this.cities.length; i++) {
          const response2 = await axios.get(
            `https://api.openweathermap.org/data/2.5/weather?q=${this.cities[i].city_name}&units=metric&appid=50fa221d32e710d1045aad7ee9da01a8`
          );
          this.infos.push(response2.data);
          // console.log(response2.data.weathers);
        }
        console.log(this.infos);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getPreviousWeather();
  },
};
</script>

<style>
.bg-color {
  background-image: radial-gradient(
    circle farthest-corner at 10% 20%,
    rgba(97, 186, 255, 1) 0%,
    rgba(166, 239, 253, 1) 90.1%
  );
  height: 2000px;
}

.wrapper {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1em;
}
.flex {
  display: flex;
  flex-direction: row;
}
.input-size {
  margin: auto;
  width: 50%;
}
.main-nav {
  padding-top: 50px;
}
.align {
  position: relative;
  top: 50%;
  transform: translateY(50%);
}
</style>

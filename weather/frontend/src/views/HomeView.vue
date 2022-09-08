<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <input v-model="city_query" type="text" name="" id="" />
      <button type="submit">Search</button>
    </form>
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
    };
  },
  computed: {},
  methods: {
    async onSubmit() {
      await this.getWeather();

      let endpoint = "/api/";
      try {
        const response = await axios.post(endpoint, {
          city_name: this.city_query,
        });
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getWeather() {
      let endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${this.city_query}&units=metric&appid=50fa221d32e710d1045aad7ee9da01a8`;

      try {
        const response = await axios.get(endpoint);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
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
.wrapper {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1em;
  grid-auto-rows: minmax(1000px, auto);
}
</style>

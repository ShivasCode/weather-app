<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <input v-model="city_query" type="text" name="" id="" />
      <button type="submit">Search</button>
    </form>

    <div v-for="info in infos.weather">{{ info.main }}</div>
    {{ infos.name }}
    <div v-for="weather in infos.weathers">{{ weather.description }}</div>
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
      infos: {
        main: {},
        sys: {},
        weather: [],
      },
      cities: [],
      name: {},
    };
  },
  methods: {
    async onSubmit() {
      await this.getWeather();

      let endpoint = "/api/";
      try {
        const response = await axios.post(endpoint, {
          name: this.city_query,
        });
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getWeather() {
      let endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${this.city_query}&appid=50fa221d32e710d1045aad7ee9da01a8`;

      try {
        const response = await axios.get(endpoint);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getPreviousWeather() {
      let endpoint = "/api/";

      try {
        const response1 = await axios.get(endpoint);

        this.cities = response1.data;
        for (let i = 0; i < this.cities.length; i++) {
          const response2 = await axios.get(
            `https://api.openweathermap.org/data/2.5/weather?q=${this.cities[i].city_name}&appid=50fa221d32e710d1045aad7ee9da01a8`
          );
          this.infos = response2.data;
          this.weathers = response2.data.weather;
          console.log(response2.data);
          // console.log(response2.data.weathers);
        }
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

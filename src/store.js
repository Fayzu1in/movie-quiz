import { defineStore } from "pinia";

export const useQuizStore = defineStore("quiz", {
  state: () => ({
    score: 100,
  }),
});

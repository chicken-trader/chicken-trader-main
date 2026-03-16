import { defineStore } from "pinia";
import { api } from "./api";

export const useThesisStore = defineStore("theses", {
  state: () => ({
    items: [] as any[],
    error: "",
    loading: false,
  }),
  actions: {
    async load() {
      this.error = "";
      this.loading = true;
      try { this.items = await api("/theses"); }
      catch (e: any) { this.error = e.message; }
      finally { this.loading = false; }
    },
    async unfollow(id: number) {
      await api(`/theses/${id}`, { method: "DELETE" });
      this.items = this.items.filter((t: any) => t.id !== id);
    },
  },
});

import { defineStore } from "pinia";
import { api } from "./api";

export const useNotificationsStore = defineStore("notifications", {
  state: () => ({
    items: [] as any[],
    error: "",
    loading: false,
  }),
  getters: {
    unreadCount: (state) => state.items.filter((n) => !n.read).length,
  },
  actions: {
    async load() {
      this.error = "";
      this.loading = true;
      try { this.items = await api("/notifications"); }
      catch (e: any) { this.error = e.message; }
      finally { this.loading = false; }
    },
    async markRead(id: number) {
      try {
        await api(`/notifications/${id}/read`, { method: "POST" });
        const item = this.items.find((n) => n.id === id);
        if (item) item.read = true;
      } catch (e: any) {
        this.error = e.message;
      }
    },
    async markAllRead() {
      const unread = this.items.filter((n) => !n.read);
      await Promise.all(unread.map((n) => this.markRead(n.id)));
    },
  },
});

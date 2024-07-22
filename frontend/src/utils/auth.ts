import { ACCESS_TOKEN, REFRESH_TOKEN } from "./constants";

export const getAuthToken = () => localStorage.getItem(ACCESS_TOKEN)
export const getRefreshToken = () =>localStorage.getItem(REFRESH_TOKEN)
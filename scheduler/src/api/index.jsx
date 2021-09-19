import axios from 'axios';

export const API = axios.create({
  baseURL: 'https://kdsp-portal.herokuapp.com/',
});

export const Mock = axios.create({
  baseURL: 'https://6cf5b666-d088-4bfd-a48b-0f9942d165e0.mock.pstmn.io',
});

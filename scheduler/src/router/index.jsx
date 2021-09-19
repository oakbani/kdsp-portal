import React from 'react';
import {  CssBaseline } from '@material-ui/core';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Dashboard from '../pages/dashboard';

export default function Router() {
    return (
          <BrowserRouter>
            <CssBaseline />
            <Switch>
              <Route path="/">
                  <Dashboard />
              </Route>
            </Switch>
          </BrowserRouter>
      )
    
  }
  
import React from "react";
import { createStyles, makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import logo from "assest/images/logo.png";

const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      flexGrow: 1,
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
      textAlign: "center",
    },
    logo: {
      maxWidth: 45,
      marginRight: "10px",
    },
    appbar: {
      backgroundColor: '#0f111e'

    },
  })
);

export default function ButtonAppBar() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.appbar}>
        <Toolbar>
          <img src={logo} alt="" className={classes.logo} />
          <Typography variant="h6" className={classes.title}>
            Karachi Down Syndrome Program
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}

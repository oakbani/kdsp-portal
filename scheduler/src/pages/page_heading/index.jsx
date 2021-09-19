import { makeStyles } from '@material-ui/core/styles';
import { Grid, Typography, CssBaseline } from '@material-ui/core';
import React from 'react';
import PropTypes from 'prop-types';

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: theme.spacing(2),
  },
  header: {
    fontWeight: theme.typography.fontWeightBold,
    marginTop: theme.spacing(2),
  },
  logoDiv: {
    position: 'relative',
    top: '8px',
    right: '8px',
    float: 'right',
    marginRight: '10px',
    marginTop: '15px',
  },
  pageLogo: {
    height: '10vmin',
    width: '20vmin',
    alignItems: 'right',
  },
}));

function PageHeader({ title }) {
  const classes = useStyles();
  return (
    <Typography variant="h5" component="h4" className={classes.header}>
      {title}
    </Typography>
  );
}

PageHeader.propTypes = {
  title: PropTypes.string.isRequired,
};

function PageParagraph({ description }) {
  return (
    <Typography variant="subtitle2" component="p">
      {description}
    </Typography>
  );
}

PageParagraph.propTypes = {
  description: PropTypes.string.isRequired,
};

function DisplayLogo({ src }) {
  const classes = useStyles();
  return (
    <Typography className={classes.logoDiv} variant="h6" color="inherit" noWrap>
      <img src={src} className={classes.pageLogo} alt="" />
    </Typography>
  );
}

DisplayLogo.propTypes = {
  src: PropTypes.string.isRequired,
};

export default function Header({ header, description, src }) {
  const classes = useStyles();
  return (
    <>
      <CssBaseline />
      <Grid container className={classes.root}>
        <Grid item xs={6}>
          <PageHeader title={header} />
          {description ? <PageParagraph description={description} /> : null}
        </Grid>
        <Grid item xs={6}>
          {src ? <DisplayLogo src={src} /> : null}
        </Grid>
      </Grid>
    </>
  );
}

Header.defaultProps = {
  description: null,
  src: null,
};

Header.propTypes = {
  header: PropTypes.string.isRequired,
  description: PropTypes.string,
  src: PropTypes.string,
};

import React from 'react';
import {
  Grid,
  FormControl,
  Select,
  MenuItem,
  FormLabel,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';

const useStyles = makeStyles((theme) => ({
  formControl: {
    flex: 1,
    width: '20em',
    maxWidth: '100%',
    borderRadius: 4,
    position: 'relative',
    backgroundColor: theme.palette.background.paper,
    border: '1px solid #ced4da',
    fontSize: 16,
    padding: '5px',
    transition: theme.transitions.create(['border-color', 'box-shadow']),
  },
  formSelector: {
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(4),
  },
  formLabel: {
    margin: 'auto 0',
  },
}));

export default function FormSelection({
  therapistList,
  handleFormChange
}) {
  // @ts-ignore
  const classes = useStyles();
  const [form, setForm] = React.useState('');

  const handleChange = (event) => {
    const formId = event.target.value;
    setForm(formId);
    handleFormChange(formId);
  };
  return (
    <Grid container spacing={1} className={classes.formSelector}>
      <Grid item xs={4} className={classes.formLabel}>
        <FormLabel component="label">
          Select therapist to book an appointment: {' '}
        </FormLabel>
      </Grid>
      <Grid item xs={8}>
        <FormControl className={classes.formControl}>
          <Select
            id="formID"
            value={form}
            onChange={handleChange}
            label="Age"
            inputProps={{ 'aria-label': 'Without label' }}
            displayEmpty
            disableUnderline
          >
            <MenuItem value="" disabled>
              Select Therapist
            </MenuItem>
            {therapistList.map((therapist) => (
              <MenuItem
                value={therapist.id}
                key={therapist.id}
              >
                {therapist.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
    </Grid>
  );
}
FormSelection.propTypes = {
  therapistList : PropTypes.arrayOf(PropTypes.object).isRequired,
  handleFormChange: PropTypes.func,
};

FormSelection.defaultProps = {
  handleFormChange: () => {},
};

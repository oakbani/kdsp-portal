import React, { useEffect, useState } from "react";
import { API,
  // Mock 
} from "api";
import {
  CssBaseline,
  Container,
  Backdrop,
  CircularProgress,
} from "@material-ui/core";
import Header from "pages/page_heading";
import ButtonAppBar from "pages/navbar";
import FormSelection from "pages/dashboard/form_selection";
import Schedular from "pages/dashboard/schedular";
// import { appointments } from "common/data";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: "#fff",
  },
}));

export default function Dashboard() {
  const classes = useStyles();
  const header = "Schedule Appointment";
  const description = null;
  const logoSrc = null;

  const [therapist, setTherapist] = useState([]);
  const [selectedId, setSelectedId] = useState(0);
  const [loader, setLoader] = useState(true);
  const [appointment, setAppointments] = useState([]);
  const fetchTherapist = () => {
    API.get("therapy/therapists").then((res) => {
      setTherapist(res.data);
    });
    // API.get("clients").then((res) => {
    //   setTherapist(res.data);
    // });
  };


  useEffect(() => {
    fetchTherapist();
    setLoader(false);
  }, []);

  useEffect(() => {
    if(selectedId!==0){
      
    API.get('therapy/slot/therapistid',{
    // Mock.get('appointment',{
      params: {
        id: selectedId,
      }
    }).then((res) => {
      const resData=res.data.slots;
      resData.map((itm,i) => {
        const obj={};
        obj.id=itm.id;
        obj.title=itm.title;
        obj.clientId=itm.client_id;
        obj.status=itm.status;
        const strtTime = itm.start_time.split(':')
        obj.startDate = new Date(itm.date);
        obj.startDate.setHours(strtTime[0]);
        obj.startDate.setMinutes(strtTime[1]);
        const endTime = itm.end_time.split(':')
        obj.endDate = new Date(itm.date);
        obj.endDate.setHours(endTime[0]);
        obj.endDate.setMinutes(endTime[1]);
        obj.type=itm.type;
        resData[i]=obj;
        return itm;
      });
      setAppointments(resData);
    });
  }
  }, [selectedId]);

  const handleFormChange = (therapistId) => {
    setSelectedId(therapistId);
  };
  return (
    <>
      <CssBaseline />
      <ButtonAppBar />
      <Backdrop className={classes.backdrop} open={loader}>
        <CircularProgress color="inherit" />
      </Backdrop>
      <Container maxWidth="lg">
        <Header header={header} description={description} src={logoSrc} />

        <FormSelection
          therapistList={therapist}
          handleFormChange={(e) => handleFormChange(e)}
        />
        <Schedular
          selectedTherapist={selectedId}
          appointments={appointment}
        />
        <CssBaseline />
      </Container>
    </>
  );
}

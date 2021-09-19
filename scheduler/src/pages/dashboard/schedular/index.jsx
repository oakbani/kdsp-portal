import React, { useState, useEffect } from "react";
import {  API } from "api";

import PropTypes from "prop-types";
import Paper from "@material-ui/core/Paper";
import { ViewState, EditingState } from "@devexpress/dx-react-scheduler";
import {
  Scheduler,
  Resources,
  DayView,
  MonthView,
  WeekView,
  Appointments,
  AppointmentTooltip,
  AppointmentForm,
  EditRecurrenceMenu,
  DragDropProvider,
  Toolbar,
  ViewSwitcher,
  DateNavigator,
  TodayButton,
} from "@devexpress/dx-react-scheduler-material-ui";
import { status, type } from "common/data";

/* eslint-disable */
const BooleanEditor = (props) => {
  return <AppointmentForm.BooleanEditor {...props} readOnly />;
};
/* eslist-enable */

const Schedular = (props) => {
  const { appointments, selectedTherapist } = props;
  const [clients, setClients] = useState([]);
  const [resources, setResources] = useState([]);
  const [currentDate, setCurrentDate] = useState(new Date());
  const [currentViewName, setCurrentViewName] = useState("Week");
  const [data, setData] = useState(appointments);

  const currentViewNameChange = (viewName) => {
    setCurrentViewName(viewName);
  };
  const currentDateChange = (date) => {
    setCurrentDate(date);
  };
  const fetchClients = () => {
    API.get("clients").then((res) => {
      const {data}=res;
      const resData = data.map((m) => ({
        ...m,
        text: m.name,
      }));
      setClients(resData);
      setResources([
        {
          fieldName: "status",
          title: "Status",
          instances: status,
        },
        {
          fieldName: "clientId",
          title: "Client",
          instances: resData,
        },
        {
          fieldName: "type",
          title: "Therapy Type",
          instances: type,
        },
      ]);
    });
  };

  useEffect(() => {
    fetchClients();
    setData(appointments);
  }, [appointments]);

  const getFormatedTime = (time) => {
    const strthr = time.getHours();
    const strtminute = time.getMinutes();
    return `${strthr}:${strtminute}:00`;
  };
  const getFormatedDate = (date) => {
    const month = date.getUTCMonth() + 1;
    const day = date.getUTCDate();
    const year = date.getUTCFullYear();
    return `${year}-${month}-${day}`;
  };
  const addRecord = (added) => {
    const obj = {
      therapist_id: selectedTherapist.toString(),
      title: added.title,
      status:
        added.status === 0 || added.status === 1
          ? added.status.toString()
          : null,
      client_id: added.clientId ? added.clientId.toString() : null,
      start_time: getFormatedTime(added.startDate),
      end_time: getFormatedTime(added.endDate),
      date: getFormatedDate(added.startDate),
      type: added.clientId ? added.clientId.toString() : null,
    };
    // console.log("add obj", obj);
    API.post("therapy/slot/add", obj);
  };

  const UpdateRecord = (added) => {
    const obj = {
      id: added.id.toString(),
      therapist_id: selectedTherapist.toString(),
      title: added.title,
      status:
        added.status === 1 || added.status === 2
          ? added.status.toString()
          : null,
      client_id: added.clientId ? added.clientId.toString() : null,
      start_time: getFormatedTime(added.startDate),
      end_time: getFormatedTime(added.endDate),
      date: getFormatedDate(added.startDate),
      type: added.clientId ? added.clientId.toString() : null,
    };
    // console.log("upd obj", obj);
    API.post("therapy/slot/update", obj);
  };

  const commitChanges = (state) => {
    const { added, changed, deleted } = state;

    if (added) {
      const startingAddedId =
        data.length > 0 ? data[data.length - 1].id + 1 : 0;
      setData([...data, { id: startingAddedId, ...added }]);
      addRecord(added);
    }
    if (changed) {
      setData(
        data.map((appointment) =>
          changed[appointment.id]
            ? { ...appointment, ...changed[appointment.id] }
            : appointment
        )
      );
      data.map((appointment) => {
        if (changed[appointment.id]) {
          UpdateRecord({ ...appointment, ...changed[appointment.id] });
          return { ...appointment, ...changed[appointment.id] };
        }
        return appointment;
      });
    }
    if (deleted !== undefined) {
      setData(data.filter((appointment) => appointment.id !== deleted));
      API.post("therapy/slot/delete", {id:deleted.toString()});
    }
    return { data };
  };

  return (
    <Paper>
      <Scheduler data={data}>
        <ViewState
          defaultCurrentDate={currentDate}
          onCurrentDateChange={currentDateChange}
          currentViewName={currentViewName}
          onCurrentViewNameChange={currentViewNameChange}
        />
        <EditingState onCommitChanges={commitChanges} />
        <EditRecurrenceMenu />
        <DayView startDayHour={9} endDayHour={24} />
        <WeekView startDayHour={9} endDayHour={24} />
        <MonthView />
        <Toolbar />
        <DateNavigator />
        <TodayButton />
        <ViewSwitcher />
        <Appointments />
        <AppointmentTooltip showOpenButton showDeleteButton />
        <AppointmentForm booleanEditorComponent={BooleanEditor} />

        <Resources data={resources} />
        <DragDropProvider />
      </Scheduler>
    </Paper>
  );
};

Schedular.propTypes = {
  appointments: PropTypes.arrayOf(PropTypes.object).isRequired,
  selectedTherapist: PropTypes.number.isRequired,
};

Schedular.defaultProps = {};
export default Schedular;

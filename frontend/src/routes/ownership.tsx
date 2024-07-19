import { Box, Button, Input, Paper, Stack, TextField, Typography } from '@mui/material'
import React from 'react'
import { Form, redirect } from 'react-router-dom'
import api from '../utils/api';

export async function action({ request }: { request: Request }) {
  const formData = await request.formData();
  const ownership = Object.fromEntries(formData);
  console.log(ownership)
  let peopleNull = false
  if (ownership.first_name === ""
    && ownership.last_name === ""
    && ownership.address === ""
    && ownership.dob === ""
    && ownership.license === ""
  ) {
    peopleNull = true
  }
  const response = await api.post('/api/ownership/', {
    people: peopleNull ? null : {
      first_name: ownership.first_name,
      last_name: ownership.last_name,
      address: ownership.address,
      dob: ownership.dob,
      license: ownership.license
    },
    vehicle: {
      make: ownership.make,
      model: ownership.model,
      color: ownership.color,
      plate_number: ownership.plate_number
    }
  })
  console.log(response)
  return redirect("/vehicle")

}

const Ownership = () => {
  return (
    <Form method='post'>
      <Stack
        direction="row"
        justifyContent="center"
        alignItems="flex-start"
        spacing={4}
      >
        <Stack
          direction="column"
          justifyContent="center"
          alignItems="center"
          spacing={1}
        >
          <TextField id="standard-basic" variant="outlined" label='First Name' name='first_name' placeholder='First Name' />
          <TextField id="standard-basic" variant="outlined" label='Last Name' name='last_name' placeholder='Last Name' />
          <TextField id="standard-basic" variant="outlined" label='Date of Birth' name='dob' placeholder='Date of Birth' />
          <TextField id="standard-basic" variant="outlined" label='License' name='license' placeholder='License' />
          <TextField id="standard-basic" variant="outlined" label='Address' name='address' placeholder='Address' />

          <TextField id="standard-basic" variant="outlined" label='Make' name='make' placeholder='vehicle make' />
          <TextField id="standard-basic" variant="outlined" label='Model' name='model' placeholder='model' />
          <TextField id="standard-basic" variant="outlined" label='Color' name='color' placeholder='Color' />
          <TextField id="standard-basic" variant="outlined" inputProps={{ maxLength: 7, minLength: 7 }} label='Plate Number' name='plate_number' placeholder='Plate Number' />
          <Button fullWidth className='h-14' variant="outlined" type='submit'>Submit</Button>
        </Stack>
      </Stack>
    </Form>
  )
}

export default Ownership
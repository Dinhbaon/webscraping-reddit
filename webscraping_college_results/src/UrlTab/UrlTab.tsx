import { ChangeEvent, useContext, useState } from "react"
import { DataContext } from "../context"
import useApplyFilters from "../Filters/useApplyFilters"
import { Typography } from "@mui/material"
import CloseIcon from '@mui/icons-material/Close';
const UrlTab = ({loUrl, setOpened} : {loUrl : string[], setOpened: React.Dispatch<React.SetStateAction<boolean>>}) => {

    const loUrlComponent = loUrl.map((url) =>
         <li>
            <a style={{textDecoration: 'none'}}href={url} target="_blank">
                <Typography>
                    {url}
                </Typography>
            </a>
        </li>)
    const closeTab =(event: React.ChangeEvent<HTMLInputElement>):void => {
        
        setOpened(false)
    }

    

    return (

        <div> 
            <div onClick={()=>closeTab} style={{margin: '5px 0px 0px 5px', position: 'absolute'}}>
                <CloseIcon/>
            </div>
            
            <ul style={{listStyle: 'none' }}>
                {loUrlComponent}
            </ul>
        </div>
    )

}

export default UrlTab
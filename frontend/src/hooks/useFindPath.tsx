import { useEffect, useState } from "react";
import { Location, useLocation } from "react-router-dom";

export const useFindPath = () => {
    const location: Location = useLocation();
    const [currentPath, setCurrentPath] = useState<string>();
    useEffect(() => {
        setCurrentPath(location.pathname);
    }, [location]);
    return currentPath;
};
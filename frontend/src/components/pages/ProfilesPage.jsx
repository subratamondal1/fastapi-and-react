import { NavLink, Outlet } from "react-router-dom";

function ProfilesPage() {
  const profiles = [1, 2, 3, 4, 5];
  return (
    <div className="flex gap-2">
      <div className="flex flex-col justify-center items-center text-5xl space-y-10">
        {profiles.map((profile) => (
          <NavLink
            className={({ isActive }) => {
              return isActive && "text-blue-500";
            }}
            key={profile}
            to={`/profiles/${profile}`}>
            <h1>Profile: {profile}</h1>
          </NavLink>
        ))}
      </div>
      <Outlet />
    </div>
  );
}

export default ProfilesPage;

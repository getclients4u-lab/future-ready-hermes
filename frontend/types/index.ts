export interface User {
  id: string;
  email: string;
  full_name: string | null;
  is_active: boolean;
  role: string;
}

export interface Project {
  id: string;
  name: string;
  description: string | null;
  status: "draft" | "in_progress" | "review" | "completed" | "archived";
  created_at: string;
  updated_at: string;
}

export interface Report {
  id: string;
  project_id: string;
  format: "pdf" | "json";
  status: "queued" | "processing" | "completed" | "failed";
  download_url: string | null;
  created_at: string;
}
